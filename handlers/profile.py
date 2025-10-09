from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import profile

router = Router() 

@router.callback_query(F.data == 'profile')
async def profile_def(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
    "<b>Настройки профиля 👤</b>\nID:991324\nИмя:Антон\nТариф: Месяц\nДата окончания подписки: 8/11/2025\nАвтоплатёж: Подключен",
        parse_mode='html',
        reply_markup=profile.profile_kb.as_markup()
    )
