from fastapi import APIRouter
from service.database import get_users as get_users_service


router = APIRouter(prefix="/users", tags=['users'])

@router.get("/get_users")
async def get_users():
    users = await get_users_service()
    return {"users": users, "count": len(users)}

@router.post("/add_user")
async def add_user(chat_id: int, username: str):
    user = await add_user(chat_id, username)
    return user