from typing import Sequence
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.database.database_manager import get_async_session
from src.models.v1.users import Permission
from src.repositories.permission_repository import PermissionRepository


class PermissionService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.repository = PermissionRepository(self.session)

    async def get_all(self) -> Sequence[Permission]:
        return await self.repository.get_all()

    async def get_permission_or_404(self, permission_id: str) -> Permission:
        permission = await self.repository.get(permission_id)

        if not permission:
            raise HTTPException(
                status_code=404, detail=f"Permission with id ({permission_id}) not found")

        return permission
