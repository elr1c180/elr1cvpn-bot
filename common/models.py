from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Boolean, ForeignKey

import os

DATABASE_URL = os.environ.get("DATABASE_URL")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    username = Column(String, index=True)
    chat_id = Column(BigInteger, primary_key=True, unique=True, index=True)
    tariff = Column(Integer, ForeignKey("Tariff.id"))
    name = Column(String)
    autopay = Column(Boolean, default=False)
    expire_date = Column(DateTime)

class Tariff(Base):
    __tablename__ = "Tariff"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
