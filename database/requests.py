from sqlalchemy import insert, select, func
from config import async_session
from database.models import ResourceTypes, UserAnimals, UserResources, Users
from sqlalchemy import update

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

async def buy_chicken(userid:int):
    async with async_session as session:
        eweae= UserResources(user_id=userid, resource_id=1, amount=-300)
        session.add(eweae)
        userAnimal =  UserAnimals(user_id=userid, animal_id=1, amount=1)
        session.add(userAnimal)
        await session.commit()