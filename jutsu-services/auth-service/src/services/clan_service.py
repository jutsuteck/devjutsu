from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.database.database_manager import get_async_session
from src.models.v1.users import Clan
from src.repositories.clan_repository import ClanRepository


class ClanService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.clan_repository = ClanRepository(self.session)

    async def create_clan(self, clan_data: dict) -> Clan:
        clan = Clan(**clan_data)
        await self.clan_repository.add(clan)

        return clan

    async def get_clan_or_404(self, clan_id: str) -> Clan:
        clan = await self.clan_repository.get(clan_id)

        if not clan:
            raise HTTPException(
                status_code=404, detail=f"Clan with id ({clan_id}) not found")

        return clan

    async def update_clan(self, clan_id: str, clan_data: dict) -> Clan:
        await self.get_clan_or_404(clan_id)
        updated_clan = await self.clan_repository.update(clan_id, clan_data)
        return updated_clan

    async def delete_clan(self, clan_id: str) -> None:
        await self.get_clan_or_404(clan_id)
        await self.clan_repository.delete(clan_id)
