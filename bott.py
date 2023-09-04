import asyncio
from aiogram import Bot, Dispatcher

from data import morning_wishes, compliments
import random
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
import os
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.callback_query import CallbackQuery
import handlers as handlers
import aiohttp

logging.basicConfig(level=logging.DEBUG)


def get_morning():
    return random.choice(morning_wishes)


def get_compliment():
    return random.choice(compliments)


admins = {
    'pozzy21': True,
}

arina = {
    'desartik': True,
    'pozzy22': True,
}

# id Arina - 902094738


async def send_message_with_text():
    message_text = f'{random.choice(morning_wishes)}'

    # Ваш код для отправки сообщения с текстом пользователю
    async with aiohttp.ClientSession() as session:
        url = f"https://api.telegram.org/bot6604631975:AAHWumcZp1_cqXYwf-mIH40GS6bHNaQ-P9o/sendMessage"
        params = {
            "chat_id": 902094738,
            "text": message_text
        }
        async with session.get(url, params=params) as response:
            # Обработка ответа, если необходимо
            pass


async def schedule_token_update():
    while True:
        await asyncio.sleep(60*60*24)
        # Время, за которое вы хотите обновить токен до его истечения
        print('Hello World!')
        update_time = 1 * 60  # 45 минут в секундах

        # Ожидание перед запуском обновления токена
        # await asyncio.sleep(update_time)
        await send_message_with_text()
        # Запуск обновления токена


async def main():
    bot = Bot(token="6604631975:AAHWumcZp1_cqXYwf-mIH40GS6bHNaQ-P9o")
    dp = Dispatcher()
    dp.include_routers(handlers.router)
    asyncio.create_task(schedule_token_update())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
