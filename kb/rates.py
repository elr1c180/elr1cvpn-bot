from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from aiogram.types import WebAppInfo

rates = InlineKeyboardBuilder()

rates.add(
    types.InlineKeyboardButton(
        text="🕐 7 дней - 75 ₽",
        callback_data="week"
    )
)

rates.add(
    types.InlineKeyboardButton(
        text="📅 Месяц - 260 ₽",
        callback_data="month"
    )
)

rates.add(
    types.InlineKeyboardButton(
        text="🎯 Годовой тариф - 2.699 ₽",
        callback_data="year"
    )
)

rates.add(
    types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="start"
    )
)

rates.adjust(1)



webapp = InlineKeyboardBuilder()

webapp.add(
    types.InlineKeyboardButton(
        text="Подключиться",
        web_app=WebAppInfo(url="https://elr1c.ru/")
    )
)

