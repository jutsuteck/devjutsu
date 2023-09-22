from fastapi import APIRouter, Depends

from src.schemas.v1.clan_schemas import (
    ClanCreateSchema,
    ClanReadSchema,
    ClanUpdateSchema
)
from src.services.clan_service import ClanService

router = APIRouter()


@router.post('/new', response_model=ClanReadSchema)
async def create_clan(
        clan_create_schema: ClanCreateSchema,
        service: ClanService = Depends(ClanService)):
    return await service.create_clan(clan_create_schema.model_dump())


@router.get('/{clan_id}', response_model=ClanReadSchema)
async def get_clan_by_id(
        clan_id: str, service:
        ClanService = Depends(ClanService)):
    return await service.get_clan_or_404(clan_id)


@router.patch('/update/{clan_id}', response_model=ClanReadSchema)
async def update_clan(
        clan_id: str,
        clan_update_schema: ClanUpdateSchema,
        service: ClanService = Depends(ClanService)):
    return await service.update_clan(clan_id, clan_update_schema.model_dump())


@router.delete('/delete/{clan_id}')
async def delete_clan(
        clan_id: str,
        service: ClanService = Depends(ClanService)):
    return await service.delete_clan(clan_id)
