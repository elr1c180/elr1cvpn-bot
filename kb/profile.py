from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

profile_kb = InlineKeyboardBuilder()

profile_kb.add(
    types.InlineKeyboardButton(
        text='Отключить автоплатёж',
        callback_data='autopay_cancel'
    )
)

profile_kb.adjust(1)