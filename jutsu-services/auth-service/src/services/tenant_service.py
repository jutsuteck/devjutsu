from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.database.database_manager import get_async_session
from src.models.v1.users import Tenant
from src.repositories.tenant_repository import TenantRepository


class TenantService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.repository = TenantRepository(self.session)

    async def create_tenant(self, tenant_data: dict) -> Tenant:
        tenant = Tenant(**tenant_data)
        return await self.repository.add(tenant)

    async def get_tenant_or_404(self, tenant_id: str) -> Tenant:
        tenant = await self.repository.get(tenant_id)

        if not tenant:
            raise HTTPException(
                status_code=404,
                detail=f"Tenant with id ({tenant_id}) not found"
            )

        return tenant

    async def delete_tenant(self, tenant_id: str) -> None:
        tenant = await self.get_tenant_or_404(tenant_id)
        await self.repository.delete(tenant)
