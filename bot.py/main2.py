from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menyu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Taomlar'),KeyboardButton(text='Ichimliklar'),KeyboardButton(text='Shirinlik')],
        [KeyboardButton(text='Aloqa')],
    ],
    resize_keyboard=True
)

taomlar2=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Osh'),KeyboardButton(text='Lavash'),KeyboardButton(text='KFC')],
        [KeyboardButton(text='Shashlik'),KeyboardButton(text='Burger'),KeyboardButton(text='Ortga')],
    ],
    resize_keyboard=True
)
