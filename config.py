from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from tokens import VK_API_TOKEN


#bot part
api = API(VK_API_TOKEN)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()


#sql
# config.py

engine = create_async_engine("sqlite+aiosqlite:///test.db")
async_session = async_sessionmaker(engine, expire_on_commit=False)
async_session: AsyncSession = async_session()