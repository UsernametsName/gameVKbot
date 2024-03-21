from vkbottle import BaseStateGroup
from vkbottle.bot import BotLabeler, rules, Message
from vkbottle_types.objects import UsersUserFull
from vkbottle.bot import rules

from database.requests import get_resources
from keyboards import k_main, k_Farm


private_labeler = BotLabeler()

@private_labeler.private_message(command="start")
async def start_command(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    await message.answer("Приветствую тебя 😊.\nЭто игра ферма 🎮🚜, где именно ты 👈 сможешь развить своё предприятие 🏭📈.🎉", keyboard=k_main)
    resources = await get_resources(user.id)
    await message.answer(f"⭐Имя: {user.first_name} {user.last_name}\n"
                            "⚡Уровень фермы: 1\n"
                            f"💸Деньги: {resources[0][2]}\n"
                            "🌐Место по миру: 1 ")

@private_labeler.private_message(rules.PayloadRule({"btn_menu": "farm"}))
async def farm_handler(message: Message):
    await message.answer("На твоей ферме живут🐷:\n"
                            f"🐔 Курицы: {2} шт.\n"
                            f"🐄 Коровы: {1} шт.\n"
                            " \n"
                            "⌛ Пока тебя не было:\n"
                            f"Курицы слесли {0} 🥚!\n"                          #Допили эту хуйню пж
                            f"Коровы выработали {0} 🥛!", keyboard=k_Farm)      #И эту желательно