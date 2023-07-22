from typing import List
from fastapi_users.db import SQLAlchemyBaseOAuthAccountTableUUID, SQLAlchemyBaseUserTableUUID
from sqlalchemy import UUID, Column, ForeignKey, String, Table, text
from sqlalchemy.orm import Mapped, declarative_base, relationship

Base = declarative_base()


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("member.id"))


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


class Permission(Base):
    __tablename__ = "permission"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, nullable=False)
    roles = relationship('Role', secondary="role_permissions",
                         back_populates="permissions")


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

role_permissions = Table(
    'role_permissions', Base.metadata,
    Column('role_id', UUID(as_uuid=True), ForeignKey('role.id')),
    Column('permission_id', UUID(as_uuid=True), ForeignKey('permission.id'))
)
