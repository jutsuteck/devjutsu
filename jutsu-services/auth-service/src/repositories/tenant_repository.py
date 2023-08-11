from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.v1.users import Tenant


class TenantRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, tenant: Tenant) -> Tenant:
        self.session.add(tenant)
        await self.session.commit()
        return tenant

    async def get(self, tenant_id: str) -> Tenant:
        query = await self.session.execute(
            select(Tenant).
            where(Tenant.id == tenant_id))

        tenant = query.scalars().first()

        return tenant

    async def delete(self, tenant: Tenant) -> None:
        await self.session.delete(tenant)
        await self.session.commit()
