from typing import List
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID
)
from sqlalchemy import UUID, Column, ForeignKey, String, Table, text
from sqlalchemy.orm import Mapped, declarative_base, relationship

Base = declarative_base()


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey(
        "members.id"))  # type: ignore


class Member(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "members"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'))
    tenant = relationship('Tenant', back_populates='members')

    roles = relationship(
        'Role', secondary="member_roles", back_populates="members")
    teams = relationship('Team', secondary='team_members',
                         back_populates='members')
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined")


class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, nullable=False)
    permissions = relationship(
        'Permission', secondary="role_permissions", back_populates="roles")
    members = relationship(
        'Member', secondary="member_roles", back_populates="roles")


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, nullable=False)
    roles = relationship('Role', secondary="role_permissions",
                         back_populates="permissions")


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, nullable=False)
    members = relationship('Member', back_populates='tenant')
    teams = relationship("Team", back_populates="tenant")


class Team(Base):
    __tablename__ = "teams"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, index=True)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'))
    tenant = relationship('Tenant', back_populates='teams')
    members = relationship(
        'Member', secondary='team_members', back_populates='teams')


member_roles = Table(
    'member_roles', Base.metadata,
    Column('member_id', UUID(as_uuid=True), ForeignKey('members.id')),
    Column('role_id', UUID(as_uuid=True), ForeignKey('roles.id'))
)

role_permissions = Table(
    'role_permissions', Base.metadata,
    Column('role_id', UUID(as_uuid=True), ForeignKey('roles.id')),
    Column('permission_id', UUID(as_uuid=True), ForeignKey('permissions.id'))
)


team_members = Table(
    'team_members', Base.metadata,
    Column('team_id', UUID(as_uuid=True), ForeignKey('teams.id')),
    Column('member_id', UUID(as_uuid=True), ForeignKey('members.id')),
)
