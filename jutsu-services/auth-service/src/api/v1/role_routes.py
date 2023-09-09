from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.role_schemas import RoleCreateSchema, RoleReadSchema, RoleUpdateSchema
from src.services.role_service import RoleService


router = APIRouter()


@router.post('/new', response_model=RoleReadSchema)
async def create_role(
        role_create_schema: RoleCreateSchema,
        service: RoleService = Depends(RoleService)):
    return await service.create_role(role_create_schema.model_dump())


@router.get('/all', response_model=List[RoleReadSchema])
async def get_all_roles(service: RoleService = Depends(RoleService)):
    return await service.get_all()


@router.get('/member/{member_id}', response_model=RoleReadSchema)
async def get_roles_member_by_id(
        member_id: str,
        service: RoleService = Depends(RoleService)):
    return await service.filter_by_member(member_id)


@router.get('/{role_id}', response_model=RoleReadSchema)
async def get_role_by_id(
        role_id: str,
        service: RoleService = Depends(RoleService)):
    return await service.get_role_by_id_or_404(role_id)


@router.patch('/update/{role_id}', response_model=RoleReadSchema)
async def update_role(
        role_id: str,
        role_update_schema: RoleUpdateSchema,
        service: RoleService = Depends(RoleService)):
    return await service.update_role(role_id, role_update_schema.model_dump())


@router.delete('/delete/{role_id}')
async def delete_role(
        role_id: str,
        service: RoleService = Depends(RoleService)):
    await service.delete_role(role_id)
