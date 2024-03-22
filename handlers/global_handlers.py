import logging

from vkbottle import ErrorHandler
from config import labeler
from vkbottle.bot import Message
from vkbottle_types.objects import UsersUserFull

from database.requests import get_all_users

from database.models import Users

error_handler = ErrorHandler(redirect_arguments=True)
logger = logging.getLogger('vkbottle')


@labeler.message(blocking=False)
async def addUsersToDb(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    logging.getLogger("vkbottle").info(f"{user.first_name} {user.last_name} writed: {message.text}")

@labeler.message(command="users")
async def users(message: Message):
    users = await get_all_users()
    await message.answer(users)