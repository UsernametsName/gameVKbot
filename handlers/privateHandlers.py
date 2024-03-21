import random
from vkbottle.bot import BotLabeler, rules, Message
from vkbottle_types.objects import UsersUserFull
from vkbottle.bot import rules

from database.requests import get_resources, buy_chicken
from keyboards import k_main, k_Market


private_labeler = BotLabeler()




@private_labeler.private_message(command="start")
async def start_command(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    await message.answer("Приветствую тебя 😊.\nЭто игра ферма 🎮🚜, где именно ты 👈 сможешь развить своё предприятие 🏭📈.🎉", keyboard=k_main)
    resources = await get_resources(user.id)
    await message.answer(f"⭐Имя: {user.first_name} {user.last_name}\n"
                            "⚡Уровень фермы: 1\n"
                            f"💸Деньги: {resources["coin"]}\n"
                            "🌐Место по миру: 1 ")


@private_labeler.private_message(payload={"btn_menu": "profile"})
async def profile_handler(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    resources = await get_resources(user.id)
    await message.answer(f"⭐Имя: {user.first_name} {user.last_name}\n"
                            "⚡Уровень фермы: 1\n"
                            f"💸Деньги: {resources["coin"]}\n"
                            "🌐Место по миру: 1 ")
    
@private_labeler.private_message(payload={"btn_menu": "storage"})
async def storage_handler(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    resources = await get_resources(user.id)
    
    mess="⚡Твои ресурсы:\n"
    for key,value in resources.items():
        mess+=f" {key}: {value} {random.choice(("⛵","🍹","🍖","🥐","🥓"))}\n"
    await message.answer(mess) 

@private_labeler.private_message(payload={"btn_menu": "shop"})
async def shop_handler(message: Message):
    await message.answer("Магазин: ",keyboard=k_Market)

@private_labeler.private_message(payload={"btn_market":"buy_chicken"})
async def chickenBuy_handler(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    resources = await get_resources(user.id)
    if resources["coin"] >= 300:
        buy_chicken(user.id)
        await message.answer("Успешная покупка")
    else:
        await message.answer("Недостаточно денег")

@private_labeler.private_message(payload={"btn_market":"buy_chicken"})
async def chickenBuy_handler(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    resources = await get_resources(user.id)
    if resources["coin"] >= 300:
        await message.answer("Успешная покупка")
    else:
        await message.answer("Недостаточно денег")
@private_labeler.private_message(payload={"btn_market":"buy_cow"})
async def chickenBuy_handler(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    resources = await get_resources(user.id)
    if resources["coin"] >= 500:
        await message.answer("Успешная покупка")
    else:
        await message.answer("Недостаточно денег")
