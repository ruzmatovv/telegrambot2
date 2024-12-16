import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
BOT_TOKEN='7558451732:AAEcyBqFYu_SkdVIjiOShoAMpix22xr5KyU'
from main2 import *
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(photo='https://www.restroapp.com/blog/wp-content/uploads/2020/03/online-food-ordering-statistics-RestroApp.jpg',caption='Online Food ga xush kelibsiz',reply_markup=menyu)


@dp.message(F.text =='Taomlar')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://resizer.mail.ru/p/373b974d-d1ee-5874-9e10-c89f0aef5ddf/AQAGoovlKQz92dW7gj4t7o_6Kvm3KYwIM0F0AQPF-lH15hkyXRwleZCnFtTvZ_6GIokjU3LQD7Tez7D7nL8bxoyhys0.jpg',caption='Taomlardan birini tanlang',reply_markup=taomlar2)

@dp.message(F.text == 'Aloqa')
async def aloqa(message: Message):
    await message.answer(text='https://t.me/umrbek_9171',reply_markup=menyu)


@dp.message(F.text =='Osh')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/get-mpic/5366523/img_id6583256424188445360.jpeg/orig',caption='',reply_markup=taomlar2)


@dp.message(F.text =='Lavash')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/get-altay/9717139/2a00000188e2e30a8af679ea94d6d48bc52b/orig',caption='',reply_markup=taomlar2)



@dp.message(F.text =='KFC')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://medialeaks.ru/wp-content/uploads/2020/10/1-3-1-1.jpg',caption='',reply_markup=taomlar2)


@dp.message(F.text =='Shashlik')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/get-altay/6514890/2a0000017f53d1016b6c90a34943cdc491b6/XXL_height',caption='',reply_markup=taomlar2)


@dp.message(F.text =='Burger')
async def taomlar1(message: Message):
    await message.answer_photo(photo='',caption='',reply_markup=taomlar2)



@dp.message(F.text =='Ortga')
async def taomlar1(message: Message):
    await message.answer(text='Assosiy menyu',reply_markup=menyu)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
