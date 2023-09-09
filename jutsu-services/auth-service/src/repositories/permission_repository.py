from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.v1.users import Permission


class PermissionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Permission]:
        permissions = await self.session.execute(select(Permission))
        return permissions.scalars().all()

    async def get_by_id(self, permission_id: str) -> Permission:
        permission = await self.session.execute(
            select(Permission).
            where(Permission.id == permission_id))
        return permission.scalars().first()

    async def get_by_name(self, permission_name: str) -> Permission:
        query = await (
            self.session.execute(
                select(Permission).filter_by(name=permission_name))
        )
        return query.scalars().first()
