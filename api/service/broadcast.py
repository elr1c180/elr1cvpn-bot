from aiogram import Dispatcher, Bot
from common.loadenv import returnToken

BOT_TOKEN = returnToken()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def broadcast_func(chat_id, text):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text
        )
    except Exception as e:
        return {"error": str(e)}
