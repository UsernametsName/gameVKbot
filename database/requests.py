from sqlalchemy import select
from config import async_session
from database.models import Resources, Users



async def get_all_users():
    async with async_session as session:
        response = await session.scalars(select(Users))
        return response.all()

async def get_resouses(userid:int):
    async with async_session as session:
        return (await session.scalars(select(Resources).where(Resources.id == userid))).first()