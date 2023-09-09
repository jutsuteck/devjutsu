from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.v1.users import Team


class TeamRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, team: Team) -> Team:
        self.session.add(team)
        await self.session.commit()
        return team

    async def get(self, team_id: str) -> Team | None:
        query = await (
            self.session.execute(select(Team).where(Team.id == team_id))
        )
        team = query.scalars().first()

        return team

    async def update(self, team_id: str, team_data: dict) -> Team:
        query = (
            update(Team).
            where(Team.id == team_id).
            values(**team_data).
            returning(Team)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, team_id: str) -> None:
        query = delete(Team).where(Team.id == team_id)
        await self.session.execute(query)
        await self.session.commit()
