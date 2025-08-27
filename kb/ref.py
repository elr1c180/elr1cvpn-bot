from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

ref_kb = InlineKeyboardBuilder()
ref_kb.add(
    types.InlineKeyboardButton(
        text="Стать участником",
        callback_data="referal_start"
    )
)
