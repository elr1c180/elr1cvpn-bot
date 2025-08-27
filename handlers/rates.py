from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import rates, back

from pay import generate_payment_link

router = Router() 

@router.callback_query(F.data == 'rates')
async def rates_def(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
       "На выбор у нас есть следующие тарифы",
        parse_mode='html',
        reply_markup=rates.rates.as_markup()
    )
    await callback.answer()


@router.callback_query(F.data == 'week')
async def rates_def(callback: CallbackQuery):
    await callback.message.delete()
    link = generate_payment_link(float(75), "Подписка на 7 дней. ElR1C VPN", callback.from_user.id, callback.from_user.username, 'week')
    await callback.message.answer(
       f"Проведите оплату по этой <a href='{link}'>ссылке</a>",
        parse_mode='html',
        reply_markup=back.back.as_markup()
    )
    await callback.answer()

@router.callback_query(F.data == 'month')
async def rates_def(callback: CallbackQuery):
    await callback.message.delete()
    link = generate_payment_link(float(260), "Подписка на месяц. ElR1C VPN", callback.from_user.id, callback.from_user.username, 'month')
    await callback.message.answer(
       f"Проведите оплату по этой <a href='{link}'>ссылке</a>",
        parse_mode='html',
        reply_markup=back.back.as_markup()
    )
    await callback.answer()

@router.callback_query(F.data == 'year')
async def rates_def(callback: CallbackQuery):
    await callback.message.delete()
    link = generate_payment_link(float(2699), "Подписка на 12 месяцев. ElR1C VPN", callback.from_user.id, callback.from_user.username, 'year')
    await callback.message.answer(
       f"Проведите оплату по этой <a href='{link}'>ссылке</a>",
        parse_mode='html',
        reply_markup=back.back.as_markup()
    )
    await callback.answer()