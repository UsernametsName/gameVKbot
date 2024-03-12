import asyncio
import os
from config import VK_API
from vkbottle import Bot

vkbot_instance = Bot(token=VK_API)
async def main():
    vkbot_instance.run_forever()


@vkbot_instance.on.message(text=['/start'])
async def start_command(message):
    await message.answer('Привет, хуесос!')

asyncio.run(main())