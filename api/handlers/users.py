from fastapi import APIRouter
from service.database import get_users as get_users_service
from service.database import add_user as add_user_service
from service.database import delete_user as delete_user_service
from service.broadcast import broadcast_func

router = APIRouter(prefix="/users", tags=['users'])

@router.get("/get_users")
async def get_users():
    users = await get_users_service()
    return {"users": users, "count": len(users)}

@router.post("/add_user")
async def add_user(chat_id: int, username: str):
    user = await add_user_service(chat_id, username)
    return user

@router.post("/broadcast")
async def broadcast_endpoint(chat_id: int, text: str):
    msg = await broadcast_func(chat_id=chat_id, text=text)
    return {"status": msg}

@router.delete("/delete_user")
async def delete_user(chat_id: int):
    user = await delete_user_service(chat_id=chat_id)
    return {"status": user}
