from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.database.database_manager import get_async_session
from src.models.v1.users import Team
from src.repositories.team_repository import TeamRepository


class TeamService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.team_repository = TeamRepository(self.session)

    async def create_team(self, team_data: dict) -> Team:
        team = Team(**team_data)
        await self.team_repository.add(team)

        return team

    async def get_team_or_404(self, team_id: str) -> Team:
        team = await self.team_repository.get(team_id)

        if not team:
            raise HTTPException(
                status_code=404, detail=f"Team with id ({team_id}) not found")

        return team

    async def update_team(self, team_id: str, team_data: dict) -> Team:
        await self.get_team_or_404(team_id)
        updated_team = await self.team_repository.update(team_id, team_data)
        return updated_team

    async def delete_team(self, team_id: str) -> None:
        await self.get_team_or_404(team_id)
        await self.team_repository.delete(team_id)
