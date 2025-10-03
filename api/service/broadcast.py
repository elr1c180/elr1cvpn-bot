from aiogram import Dispatcher, Bot
from common.loadenv import returnToken

async def broadcast_func(chat_id, text):
    BOT_TOKEN = returnToken()
    print(BOT_TOKEN)
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text, 
            parse_mode='html'
        )
        return {"msg": "Broadcast message sent successfully to {}".format(chat_id)}
    except Exception as e:
        return {"error": str(e)}

