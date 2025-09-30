from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=['users'])


@router.get("/get_users")
async def get_users():
    return {"users": ["user1", "user2", "user3"]}