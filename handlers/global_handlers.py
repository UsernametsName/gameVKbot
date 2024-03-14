from config import labeler
from vkbottle.bot import Message



@labeler.message(text="ping")
async def ping_handler(message):
    await message.reply("pong")


@labeler.message(command="userinfo")
async def userinfo_handler(message: Message):
    user = await message.ctx_api.users.get(message.from_id)
    await message.reply(f"User info: {user}")