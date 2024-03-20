from sqlalchemy import select
from config import async_session
from database.models import Users



async def get_all_users():
    async with async_session as session:
        response = await session.scalars(select(Users))
        return response.all()
