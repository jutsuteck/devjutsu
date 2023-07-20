from fastapi import APIRouter, Depends

from src.schemas.v1.team_schema import TeamCreateSchema, TeamReadSchema, TeamUpdateSchema
from src.services.team_service import TeamService

router = APIRouter()


@router.post('/new', response_model=TeamReadSchema)
async def create_team(team_create_schema: TeamCreateSchema, service: TeamService = Depends(TeamService)):
    return await service.create_team(team_create_schema.dict())


@router.get('/{team_id}', response_model=TeamReadSchema)
async def get_team_by_id(team_id: str, service: TeamService = Depends(TeamService)):
    return await service.get_team_or_404(team_id)


@router.patch('/update/{team_id}', response_model=TeamReadSchema)
async def update_team(team_id: str, team_update_schema: TeamUpdateSchema, service: TeamService = Depends(TeamService)):
    return await service.update_team(team_id, team_update_schema.dict())


@router.delete('/delete/{team_id}')
async def delete_team(team_id: str, service: TeamService = Depends(TeamService)):
    return await service.delete_team(team_id)
