import logging

from vkbottle import ErrorHandler
from config import labeler
from vkbottle.bot import Message
from vkbottle_types.objects import UsersUserFull

from database.models import Users

error_handler = ErrorHandler(redirect_arguments=True)
logger = logging.getLogger('vkbottle')

@error_handler.register_error_handler(Exception)
async def error_bd_handler(error: Exception, message: Message, *args, **kwargs):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    logger.info(f"Пользователь {user.first_name} {user.last_name} уже есть в бд")

@labeler.message(text="ping")
async def ping_handler(message):
    await message.reply("pong")


@labeler.message(command="userinfo")
async def userinfo_handler(message: Message):
    userid = message.reply_message.from_id if message.reply_message else message.from_id
    user: UsersUserFull = (await message.ctx_api.users.get(userid))[0]
    await message.reply(f"Имя: {user.first_name}\n"
                        f"Фамилия: {user.last_name}\n"
                        f"Ссылка: https://vk.com/id{userid}\n"
                        f"id: {user.id}")
    

@labeler.message(blocking=False)
@error_handler.catch
async def addUsersToDb(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    user_db = Users(first_name=user.first_name, last_name=user.last_name, id=user.id) 
    await user_db.save()     
    print(user_db.id, user_db.first_name, user_db.last_name, message.text)
