from common.models import async_session, User
from sqlalchemy import select

async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users