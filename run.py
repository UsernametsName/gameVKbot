import asyncio
import os
from config import VK_API_TOKEN
from vkbottle import Bot
vkbot_instance = Bot(token=VK_API_TOKEN)


@vkbot_instance.on.message(text=['/start'])
async def start_command(message):
    await message.answer('Привет, хуесос!')

vkbot_instance.run_forever()
