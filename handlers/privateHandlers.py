from vkbottle import GroupEventType, GroupTypes, ShowSnackbarEvent
from vkbottle.bot import BotLabeler, rules, Message, MessageEvent
from vkbottle_types.objects import UsersUserFull
from vkbottle.bot import rules

from database.requests import BuyError, buy_animal, get_resources, get_animals, initialize_user, sell_resources
from keyboards import k_main, k_Market, k_Farm


private_labeler = BotLabeler()

async def process_buying(event: MessageEvent, animal_id:int):
    try:
        await buy_animal(user_id=event.object.user_id, animal_id=animal_id)
        await event.ctx_api.messages.send_message_event_answer( event_id=event.object.event_id,
                                                        user_id=event.object.user_id,
                                                        peer_id=event.object.peer_id,
                                                        event_data=ShowSnackbarEvent(text="Успешная покупка!").json()
                                                        )
    except(BuyError):
        await event.ctx_api.messages.send_message_event_answer( event_id=event.object.event_id,
                                                            user_id=event.object.user_id,
                                                            peer_id=event.object.peer_id,
                                                            event_data=ShowSnackbarEvent(text="Недостаточно денег на покупку :(").json()
                                                            )

@private_labeler.private_message(command="start")
async def start_command(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    await message.answer("Приветствую тебя 😊.\nЭто игра ферма 🎮🚜, где именно ты 👈 сможешь развить своё предприятие 🏭📈.🎉", keyboard=k_main)
    await initialize_user(userid=user.id, first_name=user.first_name,last_name=user.last_name )

@private_labeler.private_message(payload={"btn_menu": "profile"})
async def profile_handler(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    resources = await get_resources(user.id)
    await message.answer(f"⭐Имя: {user.first_name} {user.last_name}\n"
                            "⚡Уровень фермы: 1\n"
                            f"💸Деньги: {resources["coins"]}\n"
                            "🌐Место по миру: 1 ")
    
@private_labeler.private_message(payload={"btn_menu": "storage"})
async def storage_handler(message: Message):
    user: UsersUserFull = (await message.ctx_api.users.get(message.from_id))[0]
    resources = await get_resources(user.id)
    
    mess="⚡Твои ресурсы:\n"
    for key,value in resources.items():
        mess+=f" {key}: {value} \n"
    await message.answer(mess) 

@private_labeler.private_message(payload={"btn_menu": "shop"})
async def shop_handler(message: Message):
    await message.answer("Магазин: ",keyboard=k_Market)

@private_labeler.raw_event(GroupEventType.MESSAGE_EVENT, MessageEvent, rules.PayloadRule({"btn_market":"buy_chicken", "animal_id":2}),)
async def chickenBuy_handler(event: MessageEvent):
    animal_id = event.object.payload["animal_id"]
    await process_buying(event, animal_id)
   
@private_labeler.raw_event(GroupEventType.MESSAGE_EVENT, MessageEvent, rules.PayloadRule({"btn_market":"buy_cow", "animal_id":1}),)
async def cowBuy_handler(event: MessageEvent):
    animal_id = event.object.payload["animal_id"]
    await process_buying(event, animal_id)
  
@private_labeler.raw_event(GroupEventType.MESSAGE_EVENT, MessageEvent, rules.PayloadRule({"btn_market":"sell_all"}))
async def sell_allHandler(event: MessageEvent):
    total_income = await sell_resources(user_id=event.object.user_id)
    await event.ctx_api.messages.send_message_event_answer( event_id=event.object.event_id,
                                                            user_id=event.object.user_id,
                                                            peer_id=event.object.peer_id,
                                                            event_data=ShowSnackbarEvent(text=f"Продано ресурсов на: {total_income}").json()
    )

@private_labeler.private_message(payload={"btn_menu": "farm"})
async def farm_handler(message: Message):
    animals = await get_animals(message.from_id)
    await message.answer("На твоей ферме живут🐷:\n"
                                f"🐔 Курицы: {animals["Корова"]} шт.\n"
                                f"🐄 Коровы: {animals["Курица"]} шт.\n"
                                    
    )