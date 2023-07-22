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

    async def get(self, permission_id: str) -> Permission:
        permission = await self.session.execute(
            select(Permission).
            where(Permission.id == permission_id))
        return permission.scalars().first()
