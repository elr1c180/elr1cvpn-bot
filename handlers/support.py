from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import back

router = Router() 

@router.callback_query(F.data == 'support')
async def support_project(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
       "<b>Серверам нужно есть ;(</b>\n\nВсе Ваши ресурсы идут исключительно на улучшение работы сервиса Вы очень поможете развитию проекта своими <b>добровольными</b> пожертвованиями:\n\n<b>Ethereum</b> : <code>0x7147f9019B128C1bd70324B451A08A3DB7491A77</code>\n\n<b>USDT TRC20</b> : <code>TPP5cWVEMVVBevha6DZDSXWUHVvW2DXutw</code>\n\n<b>BTC</b> : <code>bc1qemdpwy708syd7jdqana39jf4w0w4yecmand7ff</code>\n\n<b>TON</b> : <code>UQCBj-cUMw3SXH0YJ3_BGGirw57lNlyjD4KJx8-LLwu9hyjv</code>\n\nСпасибо большое за поддержку !^-^",
        parse_mode='html',
        reply_markup=back.back.as_markup()
    )
