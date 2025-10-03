from common.models import async_session, User
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users

async def add_user(chat_id: int, username: str):
    async with async_session() as session:
        try:
            user = User(chat_id=chat_id, username=username)
            session.add(user)
            await session.commit()
            return {"status": "success", "user" : {"chat_id":chat_id, "username":username}}

        except IntegrityError as e:
            await session.rollback()
            return {"status": "error", "message": "User alredy exist"}
        
        except Exception as e:
            await session.rollback()
            return {"status": "error", "message": str(e)}