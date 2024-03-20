from vkbottle import Keyboard

from config import labeler
from vkbottle.bot import Message
from vkbottle_types.objects import UsersUserFull

@labeler.message(command = "whoami")
async def whoami(message: Message):
    userid = message.get_user
    user: UsersUserFull = (await message.ctx_api.users.get(userid))[0]
    await message.reply(f"Имя: {user.first_name}\n"
                        f"Фамилия: {user.last_name}\n"
                        f"Ссылка: https://vk.com/id{userid}\n"
                        f"id: {user.id}")
keyboard = Keyboard.add(whoami)