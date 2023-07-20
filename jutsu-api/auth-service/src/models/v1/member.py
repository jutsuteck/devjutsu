from typing import List
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import UUID, Column, ForeignKey, String, Table, text
from sqlalchemy.orm import Mapped, relationship

from src.models.v1.base import Base
from src.models.v1.oauth_account import OAuthAccount


class Member(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "member"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    roles = relationship(
        'MemberRole', secondary="member_roles", backref="members")
    teams = relationship('Team', secondary='team_members', backref='members')

    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined")


class MemberRole(Base):
    __tablename__ = "role"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, nullable=False)


team_members = Table(
    'team_members', Base.metadata,
    Column('team_id', UUID(as_uuid=True), ForeignKey('team.id')),
    Column('member_id', UUID(as_uuid=True), ForeignKey('member.id')),
)

member_roles = Table(
    'member_roles', Base.metadata,
    Column('member_id', UUID(as_uuid=True), ForeignKey('member.id')),
    Column('role_id', UUID(as_uuid=True), ForeignKey('role.id'))
)
