from typing import List
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from src.models.v1.base import Base
from src.models.v1.oauth_account import OAuthAccount


class Member(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "member"

    role = Column(String)
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined")
