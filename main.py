import asyncio
from aiogram import Dispatcher, Bot
from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from handlers import start, support, rates, ref

from kb.rates import webapp
from kb.back import back

from datetime import datetime, timedelta
import pytz
import httpx
from common.loadenv import returnToken

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from common.models import init_db

BOT_TOKEN = returnToken()

WEBHOOK_HOST = "https://elr1c.ru" # Ваш домен / domain
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URI = WEBHOOK_HOST + WEBHOOK_PATH

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(start.router, support.router, rates.router, ref.router)

    await init_db()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()

# dp.include_routers(start.router, support.router, rates.router, ref.router)

    from aiogram.fsm.context import FSMContext
    from aiogram.fsm.state import StatesGroup, State

    class NotifyUser(StatesGroup):
        chatId = State()  

    @dp.message(Command("notify"))
    async def cmd_start_notify(message: types.Message, state: FSMContext):
        await message.answer(
            f"Введите Chat ID пользователя.",
            parse_mode='html',
        )
        await state.set_state(NotifyUser.chatId)

    @dp.message(NotifyUser.chatId)
    async def process_notify_chatid(message: types.Message, state: FSMContext):
        await state.update_data(chatId=message.text)
        chatId = (await state.get_data())["chatId"]
        message_status = await notify_msg(chatId)
        await message.answer(message_status['message_status'])
        await state.clear()
    
    async def notify_msg(chatId):
        try:
            await bot.send_message(chatId,"<b>Ваша подписка заканчивается сегодня!</b>\n\nПродлите ее с помощью бота.\n\n<i>Нажмите на /start и нажмите на кнопку «Тарифы»</i>",parse_mode='html')
            return {"message_status": f"Сообщение успешно доставленно"}
        except Exception as e:
            return {"message_status": f"Ошибка при отправке: {e}"}


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """Управление жизненным циклом приложения."""
#     print("Запуск приложения...")
#     await bot.set_webhook(url=WEBHOOK_URI, drop_pending_updates=True)
#     print(f"Webhook установлен: {WEBHOOK_URI}")
#     yield
#     print("Остановка приложения...")
#     await bot.delete_webhook()
#     print("Webhook удалён.")

# app = FastAPI(lifespan=lifespan)

# @app.post("/webhook/{token}")
# async def handle_webhook(request: Request, token: str):
#     """Обработчик вебхука."""
#     if token != BOT_TOKEN:
#         print(f"Invalid token: {token}")  # Логирование некорректного токена
#         raise HTTPException(status_code=400, detail="Invalid token")
    
#     try:
#         update_data = await request.json()
        
#         # Преобразуем в объект Update
#         telegram_update = types.Update(**update_data)
        
#         await dp.feed_update(bot, telegram_update)  # Теперь передаем update и bot
        
#         return JSONResponse(content={"status": "ok"})
#     except Exception as e:
#         print(f"Error: {str(e)}")  # Логирование ошибки
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @app.post("/return_url/")
# async def payment_success(request: Request):

#     payload = await request.json()
#     print("📩 Получены данные о платеже:", payload)  # Логируем для отладки

#     if payload.get("event") == "payment.succeeded":
#         payment_id = payload["object"]["id"]
#         amount = payload["object"]["amount"]["value"]
#         user_id = payload["object"]["metadata"].get("user_id")  # ID юзера
#         username = payload["object"]["metadata"].get("username")
#         period = payload["object"]["metadata"].get("period")  # Срок подписки
#         if username == 'None':
#                 username = user_id
#         print(username)

#         print(f"✅ Платёж {payment_id} на сумму {amount} руб. прошёл успешно для юзера {user_id} на {period}")

#         await bot.send_message(user_id,'<b>Успешно!</b>\nОплата прошла, теперь вы можете получить ссылку для соединения в WebApp!', parse_mode='html', reply_markup=webapp.as_markup())

#         def check_exist(id):
#             headers = {"Content-Type": "application/json"}
#             url = 'https://elr1c.ru/api/inbounds_list'

#             params = {
#                 "id": id
#             }

#             response = httpx.get(url, params=params, headers=headers)

#             print(response.status_code)

#             try:
#                 return {"exist_status":response.json()['result'][0]['feedback'], 'expiryTime':response.json()['result'][0]['clients'][0]['expiryTime']}
#             except Exception:
#                 return {"exist_status": response.json()['result'][0]['feedback']}
        
#         def get_current_date():
#             tehran_tz = pytz.timezone("Asia/Tehran")
#             current_date_tehran = datetime.now(tehran_tz)

#             return current_date_tehran.timestamp()

#         def get_timestamp_week_ahead():
#             tehran_tz = pytz.timezone("Asia/Tehran")
#             expirytimedate = 0
#             if period == 'week':
#                 expirytimedate = 7
#             elif period == 'month':
#                 expirytimedate = 30
#             elif period == 'year':
#                 expirytimedate = 365
#             current_date_tehran = datetime.now(tehran_tz)
#             new_date_tehran = current_date_tehran + timedelta(days=expirytimedate)
#             return int(new_date_tehran.timestamp() * 1000)
        
#         def get_update_time(expiryTime):
#             tehran_tz = pytz.timezone("Asia/Tehran")
#             expiry_datetime = datetime.fromtimestamp(expiryTime / 1000, tehran_tz)
#             print(expiryTime, ' - время', type(expiryTime))
#             expirytimedate = 0
#             if period == 'week':
#                 expirytimedate = 7
#             elif period == 'month':
#                 expirytimedate = 30
#             elif period == 'year':
#                 expirytimedate = 365

#             new_date_tehran = expiry_datetime + timedelta(days=expirytimedate)
#             print(int(new_date_tehran.timestamp() * 1000))
#             return int(new_date_tehran.timestamp() * 1000)

#         def add_client(id, username):
#             url = "https://elr1c.ru/api/add_client"


#             expirytime = str(get_timestamp_week_ahead())

#             params = { 
#                 "id": str(id),
#                 "username": str(username),
#                 "expirytime": str(expirytime)
#             }

#             headers = {"Content-Type": "application/json"}

#             response = httpx.post(url, params=params, json={}, headers=headers)

#             print(response.status_code)
#             try:
#                 print(response.json())
#             except Exception:
#                 print(response.text)
        
#         def update_client(id, username, expirytime):
#             url = "https://elr1c.ru/api/update_client"


#             expirytime = str(get_timestamp_week_ahead())

#             params = { 
#                 "id": str(id),
#                 "username": str(username),
#                 "expirytime": str(expirytime)
#             }

#             headers = {"Content-Type": "application/json"}

#             response = httpx.post(url, params=params, json={}, headers=headers)

#             print(response.status_code)
#             try:
#                 print(response.json())
#             except Exception:
#                 print(response.text)

#         check = check_exist(user_id)
        
#         if check['exist_status'] == 'Client was found':
#             if int(check['expiryTime']) >= int(get_current_date() * 1000):
#                 update_client(user_id, username, int(get_update_time(int(check['expiryTime']))))
#                 print('ya tut')                
#             else:
#                 print('ya tut2')
#                 update_client(user_id, username, get_timestamp_week_ahead())           
#         else:
#             add_client(user_id, username)


        
if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8080)
    
    asyncio.run(main())