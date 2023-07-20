from typing import List
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import UUID, Column, String, text
from sqlalchemy.orm import Mapped, relationship

from src.models.v1.base import Base
from src.models.v1.oauth_account import OAuthAccount


class Member(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "member"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    roles = relationship(
        'Role', secondary="member_roles", back_populates="members")
    teams = relationship('Team', secondary='team_members',
                         back_populates='members')
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined")


class Role(Base):
    __tablename__ = "role"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, nullable=False)
    members = relationship(
        'Member', secondary="member_roles", back_populates="roles")
