import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN as token
from button import *
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(photo='https://www.restroapp.com/blog/wp-content/uploads/2020/03/online-food-ordering-statistics-RestroApp.jpg',caption='Online Food ga xush kelibsiz',reply_markup=menyu)


@dp.message(F.text =='Taomlar')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://www.restroapp.com/blog/wp-content/uploads/2020/03/online-food-ordering-statistics-RestroApp.jpg',caption='Taomlardan birini tanlang',reply_markup=taomlar2)

@dp.message(F.text == 'Aloqa')
async def aloqa(message: Message):
    await message.answer(text='https://t.me/Xudashukur',reply_markup=menyu)

@dp.message(F.text =='Osh')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://www.restroapp.com/blog/wp-content/uploads/2020/03/online-food-ordering-statistics-RestroApp.jpg',caption='',reply_markup=taomlar2)

@dp.message(F.text =='Ortga')
async def taomlar1(message: Message):
    await message.answer(text='Assosiy menyu',reply_markup=menyu)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
