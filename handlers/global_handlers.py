from config import labeler
from vkbottle.bot import Message
from vkbottle_types.objects import UsersUserFull


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