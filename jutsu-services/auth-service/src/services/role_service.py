from typing import List, Sequence
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.database.database_manager import get_async_session
from src.models.v1.users import Role
from src.repositories.role_repository import RoleRepository


class RoleService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.role_repository = RoleRepository(self.session)

    async def create_role(self, role_data: dict) -> Role:
        role = Role(**role_data)

        await self.role_repository.add(role)

        return role

    async def get_all(self) -> Sequence[Role]:
        return await self.role_repository.get_all()

    async def filter_by_member(self, member_id: str) -> List[Role]:
        member_roles = await self.role_repository.filter_by_member(member_id)

        if not member_roles:
            raise HTTPException(
                status_code=404,
                detail=f"No roles found for member with id {member_id}"
            )

        return member_roles

    async def get_role_by_id_or_404(self, role_id: str) -> Role:
        role = await self.role_repository.get_by_id(role_id)

        if not role:
            raise HTTPException(
                status_code=404,
                detail=f"Role with id ({role_id}) not found"
            )

        return role

    async def get_role_by_name_or_404(self, role_name: str) -> Role:
        role = await self.role_repository.get_by_name(role_name)

        if not role:
            raise HTTPException(
                status_code=404,
                detail=f"Role with name ({role_name}) not found"
            )

        return role

    async def update_role(self, role_id: str, role_data: dict) -> Role:
        await self.get_role_by_id_or_404(role_id)
        updated_role = await self.role_repository.update(role_id, role_data)
        return updated_role

    async def delete_role(self, role_id: str) -> None:
        await self.get_role_by_id_or_404(role_id)
        await self.role_repository.delete(role_id)
