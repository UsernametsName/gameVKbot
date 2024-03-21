from sqlalchemy import select, func
from config import async_session
from database.models import ResourceTypes, UserResources, Users

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
