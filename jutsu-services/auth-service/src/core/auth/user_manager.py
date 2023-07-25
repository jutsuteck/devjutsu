import uuid

from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from src.core.dependencies.database.database_manager import get_user_db
from src.models.v1.users import Member


class UserManager(UUIDIDMixin, BaseUserManager[Member, uuid.UUID]):
    reset_password_token_secret = "SECRET"
    verification_token_secret = "SECRET"

    async def on_after_register(
            self,
            member: Member,
            request: Optional[Request] = None):
        pass

    async def on_after_verify(
            self,
            member: Member,
            token: str, request: Optional[Request] = None) -> None:
        pass


async def get_user_manager(
        user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
