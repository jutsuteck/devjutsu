from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.v1.users import Clan


class ClanRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, clan: Clan) -> Clan:
        self.session.add(clan)
        await self.session.commit()
        return clan

    async def get(self, clan_id: str) -> Clan | None:
        query = await (
            self.session.execute(select(Clan).where(Clan.id == clan_id))
        )
        clan = query.scalars().first()

        return clan

    async def update(self, clan_id: str, clan_data: dict) -> Clan:
        query = (
            update(Clan).
            where(Clan.id == clan_id).
            values(**clan_data).
            returning(Clan)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, clan_id: str) -> None:
        query = delete(Clan).where(Clan.id == clan_id)
        await self.session.execute(query)
        await self.session.commit()
