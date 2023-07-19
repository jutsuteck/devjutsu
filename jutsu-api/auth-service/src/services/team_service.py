from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.database.database_manager import get_async_session
from src.models.v1.team import Team
from src.repositories.team_repository import TeamRepository
from src.schemas.v1.team_schema import TeamSchema


class TeamService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.team_repository = TeamRepository(self.session)

    async def create_team(self, team_data: dict):
        team = Team(**team_data)
        await self.team_repository.add(team)

        return TeamSchema(**team.__dict__)
