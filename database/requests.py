from sqlalchemy import select, func
from config import async_session
from database.models import UserResources, Users, UserAnimals

async def get_all_users():
    async with async_session as session:
        response = await session.scalars(select(Users))
        return response.all()

async def get_resources(userid:int):
    async with async_session as session:
        stmt = (select(UserResources.user_id, UserResources.resource_id, func.sum(UserResources.amount).label('total_resources'))
                .where(UserResources.user_id==userid)
                .group_by(UserResources.user_id, UserResources.resource_id))
        result = await session.execute(stmt)
        return result.fetchall()

async def get_user_animals(user_id: int):
    async with async_session() as session:
        stmt = select(UserAnimals).filter(UserAnimals.user_id == user_id)
        result = await session.execute(stmt)
        return result.scalars().all()