import re
import uuid

from typing import Optional, Union
from fastapi import Depends, Request
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, MessageType
from fastapi_users import (
    BaseUserManager,
    InvalidPasswordException,
    UUIDIDMixin
)
from fastapi_users.db import SQLAlchemyUserDatabase
from src.core.config.settings import get_settings

from src.core.dependencies.database.database_manager import get_user_db
from src.core.config.mail import smtp_connection
from src.models.v1.users import Member


class UserManager(UUIDIDMixin, BaseUserManager[Member, uuid.UUID]):
    settings = get_settings()
    reset_password_token_secret = settings.token.reset_password_token_secret
    verification_token_secret = settings.token.verification_token_secret

    async def validate_password(
            self, password: str,
            user: Union[Member, uuid.UUID]) -> None:
        """
        Validates user set password
        """
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
            request: Optional[Request] = None):

        print(member.email)

    async def on_after_request_verify(
            self,
            member: Member,
            token: str, request: Optional[Request] = None) -> None:
        print(member.email, token)

        """ message = MessageSchema( """
        """     subject="Verify", """
        """     recipients=[member.email], """
        """     body=html, """
        """     subtype=MessageType.html """
        """ ) """

        """ fm = FastMail(smtp_connection) """
        """ await fm.send_message(message) """


async def get_user_manager(
        user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
