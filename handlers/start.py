from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import start

from common.models import init_db, async_session, User
from sqlalchemy import select

router = Router() 

@router.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
    payload = command.args
    if payload:
        await message.answer(payload)
    await message.answer(
        f"<b>Здравствуйте, {message.from_user.first_name}!</b>\nДля доступа к VPN перейдите в WebApp",
        parse_mode='html',
        reply_markup=start.comm.as_markup()
    )

    telegram_id = message.from_user.id
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    name = f"{first_name} {last_name}".strip() or None
    username = message.from_user.username

    async with async_session() as session:
        result = await session.execute(select(User).where(User.chat_id == telegram_id))
        user = result.scalar_one_or_none()

        if not user:
            new_user = User(chat_id=telegram_id, username=username, name=name)
            session.add(new_user)
            await session.commit()
        else:
            pass
    

@router.callback_query(F.data == 'start')
async def cmd_start(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        f"<b>Здравствуйте, {callback.from_user.first_name}!</b>\nДля доступа к VPN перейдите в WebApp",
        parse_mode='html',
        reply_markup=start.comm.as_markup()
    )
    await callback.answer()

