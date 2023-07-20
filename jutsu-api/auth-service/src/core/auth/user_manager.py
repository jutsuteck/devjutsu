import uuid

from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from src.core.config.settings import get_settings
from src.core.dependencies.database.database_manager import get_user_db
from src.models.v1.member import Member


class UserManager(UUIDIDMixin, BaseUserManager[Member, uuid.UUID]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = get_settings()


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
