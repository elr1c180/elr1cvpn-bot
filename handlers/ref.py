from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import ref,back

router = Router() 

@router.callback_query(F.data == 'referal_system')
async def referal(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
       "<b>Прими участие в реферальной системе!</b>\n\nПолучай 45% с <b>каждой</b> оплаты твоего реферала!\n\n<a href='https://google.com'>Узнать подробности</a>",
        parse_mode='html',
        reply_markup=ref.ref_kb.as_markup()
    )


@router.callback_query(F.data == 'referal_start')
async def referal(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
       f"<b>Поздравляем!</b>\n\nТеперь вы участник реферальной программы, вы будете получать выплату за каждую оплату вашего реферала. В боте будет появляться список ваших рефералов по мере их прибытия.\n\n<b>Ваша ссылка:</b><code>https://t.me/elr1cswork_bot?start={callback.from_user.id}</code>",
        parse_mode='html',
        reply_markup=back.back.as_markup()
    )