from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler

from tokens import VK_API_TOKEN



api = API(VK_API_TOKEN)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
