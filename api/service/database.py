from common.models import async_session, User, Tariff
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError, NoResultFound

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

async def delete_user(chat_id: int):
    async with async_session() as session:
        try:
            query = delete(User).where(User.chat_id == chat_id)
            await session.execute(query)
            await session.commit()
            return {"status": "success", "User":f"User {chat_id} has been deleted"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
async def get_tariffs_service():
    async with async_session() as session:
        result = await session.execute(select(Tariff))
        tariffs = result.scalars().all()
        return tariffs

async def add_tariff_service(name: str, price: int):
    async with async_session() as session:
        try:
            tariff = Tariff(name=name, price=price)
            session.add(tariff)
            await session.commit()
            return {"status": "success", "tariff": {"name": name, "price": price}}
        
        except Exception as e:
            await session.rollback()
            return {"status": "error", "message": str(e)}