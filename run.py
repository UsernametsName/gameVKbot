from vkbottle import Bot
from config import api, state_dispenser, labeler
from handlers import chat_labeler, admin_labeler


labeler.load(chat_labeler)
labeler.load(admin_labeler)

bot = Bot(api=api, labeler=labeler, state_dispenser=state_dispenser)

bot.run_forever()