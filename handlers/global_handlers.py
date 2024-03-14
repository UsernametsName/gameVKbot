from config import labeler
from vkbottle.bot import Message
from vkbottle_types.objects import UsersUserFull


@labeler.message(text="ping")
async def ping_handler(message):
    await message.reply("pong")


@labeler.message(command="userinfo")
async def userinfo_handler(message: Message):
    userid = message.reply_message.from_id if message.reply_message else message.from_id
    user: UsersUserFull = await message.ctx_api.users.get(userid)
    await message.reply(f"Имя: {user.first_name}\n"
                        f"Фамилия: {user.last_name}\n"
                        f"Статус: {user.status}\n"
                        f"Ссылка: {user.last_seen}\n"
                        f"id: {user.id}")