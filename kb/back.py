from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

back = InlineKeyboardBuilder()
back.add(
    
    types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="start"
    )
)
