from sqlalchemy import UUID, Column, ForeignKey, Table

from src.models.v1.base import Base


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
