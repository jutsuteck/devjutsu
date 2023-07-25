from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from src.core.config.settings import get_settings
from src.models.v1.users import Member, OAuthAccount


settings = get_settings()

DB_USER = settings.postgres.postgres_user
DB_PASSWORD = settings.postgres.postgres_password
DB_NAME = settings.postgres.postgres_db
DB_HOST = settings.postgres.postgres_host
DB_PORT = settings.postgres.postgres_port

DB_URL = (
    f"postgresql+asyncpg://"
    f"{DB_USER}:"
    f"{DB_PASSWORD}@"
    f"{DB_HOST}:"
    f"{DB_PORT}/"
    f"{DB_NAME}"
)

engine = create_async_engine(DB_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, Member, OAuthAccount)
