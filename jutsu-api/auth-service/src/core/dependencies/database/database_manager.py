from collections.abc import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from src.core.dependencies.database.settings import get_settings
from src.models.v1.base import Base
from src.models.v1.user import User


class DatabaseManager:
    _instance = None
    _engine = None
    _session_maker = None
    _user_db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    @property
    def engine(self):
        if self._engine is None:
            settings = get_settings()
            DB_USER = settings.postgres_user
            DB_PASSWORD = settings.postgres_password
            DB_NAME = settings.postgres_db
            DB_HOST = settings.postgres_host
            DB_PORT = settings.postgres_port
            DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            self._engine = create_async_engine(DB_URL)

        return self._engine

    @property
    def session_maker(self):
        if self._session_maker is None:
            self._session_maker = async_sessionmaker(
                self.engine, expire_on_commit=False)
        return self._session_maker

    async def create_db_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:  # type: ignore
            yield session

    @property
    def user_db(self):
        if self.user_db is None:
            async def get_user_db(session: AsyncSession = Depends(self.get_async_session)):
                yield SQLAlchemyUserDatabase(User, session)  # type: ignore

            self._user_db = get_user_db

        return self._user_db


database_manager = DatabaseManager()
