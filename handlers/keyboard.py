from vkbottle import Keyboard, Text

from vkbottle.bot import BotLabeler
from vkbottle.bot import Message
from vkbottle_types.objects import UsersUserFull

kb_labeler = BotLabeler()

@kb_labeler.message()
async def keydef(message: Message):
    keyboard = (
        Keyboard()
        .add(Text("Кнопка 1"))
        .add(Text("Кнопка 2"))
        .row()
        .add(Text("Кнопка 3"))
    )
    await message.reply("Вот кнопочки",keyboard=keyboard)