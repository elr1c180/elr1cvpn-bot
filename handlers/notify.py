from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from kb import start

from main import notify_msg

class NotifyUser(StatesGroup):
    chatId = State()  

router = Router()

@router.message(Command("notify"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        f"Введите Chat ID пользователя.",
        parse_mode='html',
    )
    await state.set_state(NotifyUser.chatId)


@router.message(NotifyUser.chatId)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(chatId=message.text)
    chatId = await state.get_data()
    chatId = chatId["chatId"]
    print(chatId)
    message_status = await notify_msg(chatId)
    await message.answer(message_status['message_status'])
    await state.clear()