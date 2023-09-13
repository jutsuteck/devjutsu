import re
import uuid

from typing import Optional, Union
from fastapi import Depends, Request
from fastapi_users import (
    BaseUserManager,
    InvalidPasswordException,
    UUIDIDMixin
)
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.config.settings import get_settings
from src.core.dependencies.database.database_manager import (
    get_async_session,
    get_user_db
)
from src.core.enums import RolesEnum
from src.core.auth.utils import create_verification_token
from src.models.v1.users import Member
from src.services.member_service import MemberService


class UserManager(UUIDIDMixin, BaseUserManager[Member, uuid.UUID]):
    settings = get_settings()
    reset_password_token_secret = settings.token.reset_password_token_secret  # type: ignore
    verification_token_secret = settings.token.verification_token_secret  # type: ignore

    def __init__(self, user_db, member_service: MemberService):
        super().__init__(user_db)
        self.member_service = member_service

    async def validate_password(
            self, password: str,
            user: Union[Member, uuid.UUID]) -> None:
        password = re.sub('\s+', ' ', password)

        if not password.isprintable():
            raise InvalidPasswordException(
                reason="The password contains unprintable characters.")

        if len(password) < 12:
            raise InvalidPasswordException(
                reason="Password should be atleast 12 characters")

    async def on_after_register(
        self,
        member: Member,
        request: Optional[Request] = None
    ):
        # update the role after registration to "Individual User"
        await (
            self.member_service
            .update_member_role(
                member.id, RolesEnum.INDIVIDUAL_USER.value)  # type: ignore
        )

    async def on_after_request_verify(
            self,
            member: Member,
            token: str, request: Optional[Request] = None) -> None:

        verification_link = f"http://localhost:3000/login?token={token}"

        print(verification_link)


async def get_user_manager(
        user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
        session: AsyncSession = Depends(get_async_session)):
    member_service = MemberService(user_db, session)
    yield UserManager(user_db, member_service)
