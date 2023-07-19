from sqlalchemy.ext.asyncio import AsyncSession

from src.models.v1.team import Team


class TeamRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, team: Team):
        self.session.add(team)
        return await self.session.commit()
