


import os
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import  Mapped, sessionmaker

from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


class Base:
    """Base model class for resources."""

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)


DeclarativeBase: DeclarativeMeta = declarative_base(cls=Base)


class Role(DeclarativeBase):
    """Role model."""

    __tablename__ = "role"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    description = Column(String())

class User(DeclarativeBase, SQLAlchemyBaseUserTableUUID):
    """User model."""

    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    phone = Column(String(), nullable=False)
    civility = Column(String(), nullable=True)
    role: Mapped[str] = Column(String, ForeignKey("role.name"), nullable=False)







DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"






engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
