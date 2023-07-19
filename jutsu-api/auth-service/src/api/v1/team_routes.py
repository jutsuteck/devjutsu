from fastapi import APIRouter, Depends

from src.schemas.v1.team_schema import TeamCreateSchema, TeamSchema
from src.services.team_service import TeamService

router = APIRouter()


@router.post('/new', response_model=TeamSchema)
async def create_team(team_create_schema: TeamCreateSchema, service: TeamService = Depends(TeamService)):
    team = await service.create_team(team_create_schema.dict())
    return team
