import asyncio
from aiogram import Bot, Dispatcher

from data import morning_wishes, compliments
from bott import get_compliment, get_morning
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
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.callback_query import CallbackQuery
from kb import compliment
from req import get_gif

router = Router()

admins = {
    'pozzy212': True,
}

arina = {
    'desartik': True,
    'pozzy21': True,
}


@router.message(Command("start"))
async def start_handler(message: Message):
    user_login = message.from_user.username
    if user_login in admins and admins[user_login]:
        await message.answer(
            text="Привет мой создатель....",
            reply_markup=compliment()
        )
    elif user_login in arina and arina[user_login]:
        await message.answer(
            text="Привет, я помощник Паши, и я создан для того чтобы радовать тебя пока он спит и не может пожелать тебе доброго утречка как раньше! \nТак как ты запустила бота утром, с интервалом в 24 часа тебе будут отправляться доброутрошные сообщения! \nСамого доброго утречка! \n \nТы можешь нажать на появившуюся кнопочку и получишь комплимент и случайную гифку о любви!!!",
            reply_markup=compliment()
        )
        await message.answer(text="❤️❤️❤️Теперь ты будешь получать сообщения каждый день в определенное время❤️❤️❤️")

    else:
        await message.answer(
            text='Ухади....ты не Арина...'
        )
    # Добавление пользователя в список для отправки сообщений
    user_id = message.from_user.id


@router.message(F.text.lower() == "хочу комплимент")
async def send_compl(message: Message):
    await message.answer(text=str(get_compliment())
                         )
    await message.answer_animation(animation=str(get_gif()))
