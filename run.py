import asyncio
import logging
from vkbottle import Bot
from config import api, state_dispenser, labeler
from database.models import create_tables
from handlers import admin_labeler, kb_labeler


async def main() -> None:  

    labeler.load(admin_labeler)
    labeler.load(kb_labeler)
    bot = Bot(api=api, labeler=labeler, state_dispenser=state_dispenser)

    
    await create_tables()
    await bot.run_polling()


if __name__ == '__main__':
    logging.getLogger('vkbottle').setLevel(logging.DEBUG)
    logging.getLogger('aiosqlite').setLevel(logging.DEBUG)
    try:
        asyncio.run(main()) #Точка входа
    except (KeyboardInterrupt, SystemExit):
        print("EXIT")        
