from os import name
from sqlalchemy import delete, insert, select, func
from config import async_session
from database.models import Animals, ResourceTypes, UserAnimals, UserResources, Users
from sqlalchemy import update
from vkbottle import CodeException

class BuyError(Exception):
    def __init__(self, code=1, message="Недостаточно средств для покупки"):
        self.code = code
        self.message = message
        super().__init__(self.message)


async def get_all_users():
    async with async_session as session:
        response = await session.scalars(select(Users))
        return response.all()

async def get_resources(userid:int):
    async with async_session as session:
        stmt = (select(UserResources.user_id, ResourceTypes.name, func.sum(UserResources.amount).label('total_resources'))
                .where(UserResources.user_id==userid)
                .join(ResourceTypes, UserResources.resource_id == ResourceTypes.id)
                .group_by(UserResources.user_id, ResourceTypes.name))
        result = await session.execute(stmt)
        resources = {row.name: row.total_resources for row in result}
        return resources

async def initialize_user(userid:int, first_name:str, last_name:str):
    async with async_session as session:
        is_user_not_in_db = len((await session.execute(select(Users).where(Users.id == userid))).all())  == 0 
        if(is_user_not_in_db):
            resp = await session.execute(insert(Users).values(id=userid, first_name=first_name, last_name=last_name))
            await session.commit()

async def buy_animal(user_id:int, animal_id:int):
    async with async_session as session:
        # Получаем стоимость животного
        stmt = select(Animals.price).where(Animals.id == animal_id)
        result = await session.execute(stmt)
        animal_price = result.scalar_one()

        # Проверяем баланс пользователя
        stmt = select(UserResources.amount).where(UserResources.user_id == user_id, UserResources.resource_id == 1)
        result = await session.execute(stmt)
        user_balance = result.scalar_one()

        if user_balance < animal_price:
            raise BuyError()

        # Снимаем деньги с пользователя
        stmt = (
            update(UserResources).
            where(UserResources.user_id == user_id, UserResources.resource_id == 1).
            values(amount=UserResources.amount - animal_price)
        )
        await session.execute(stmt)

        # Добавляем животное пользователю
        stmt = (
            update(UserAnimals).
            where(UserAnimals.user_id == user_id, UserAnimals.animal_id == animal_id).
            values(amount=UserAnimals.amount + 1)
        )
        await session.execute(stmt)

        await session.commit()
        return True
    return False

async def sell_resources(user_id:int) ->int:
    async with async_session as session:
        # Получаем все ресурсы пользователя, кроме монет
        stmt = select(UserResources).where(UserResources.user_id == user_id, UserResources.resource_id != 1)
        user_resources = await session.execute(stmt)

        total = 0
        for user_resource in user_resources.scalars():
            # Получаем цену ресурса
            stmt = select(ResourceTypes.price).where(ResourceTypes.id == user_resource.resource_id)
            resource_price = await session.execute(stmt)
            resource_price = resource_price.scalar_one()

            # Рассчитываем общую стоимость ресурсов
            total += user_resource.amount * resource_price

            # Удаляем ресурсы пользователя
            stmt = (
                update(UserResources).
                where(UserResources.user_id == user_id, UserResources.resource_id == user_resource.resource_id).
                values(amount=0)
            )
            await session.execute(stmt)
            
        # Зачисляем деньги на счет пользователя
        stmt = (
            update(UserResources).
            where(UserResources.user_id == user_id, UserResources.resource_id == 1).
            values(amount=UserResources.amount + total)
        )
        await session.execute(stmt)
        await session.commit()
        return total
  
#FIXME 
async def get_animals(userid:int):
    async with async_session as session:
        stmt = (select(UserAnimals.user_id, Animals.name, func.sum(UserAnimals.amount).label('total_animals'))
                .where(UserAnimals.user_id==userid)
                .join(Animals, UserAnimals.animal_id == Animals.id)
                .group_by(UserAnimals.user_id, Animals.name))
        result = await session.execute(stmt)
        animals = {row.name: row.total_animals for row in result}
        return animals
