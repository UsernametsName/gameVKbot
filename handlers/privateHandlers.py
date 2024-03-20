from vkbottle.bot import BotLabeler, rules, Message
from vkbottle_types.objects import UsersUserFull

from database.models import Resources
from database.requests import get_resouses



private_labeler = BotLabeler()


@private_labeler.private_message(command="start")
async def start_command(message: Message):
    await message.answer("Приветствую тебя 😊.\nЭто игра ферма 🎮🚜, где именно ты 👈 сможешь развить своё предприятие 🏭📈.🎉")
    resourses = await get_resouses(message.from_id)
    await message.answer(f"Монет: {resourses.coins}\nЯиц: {resourses.eggs}\n")