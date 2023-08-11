from fastapi import APIRouter, Depends

from src.schemas.v1.permission_schemas import PermissionReadSchema
from src.services.permission_service import PermissionService


router = APIRouter()


@router.get('/', response_model=PermissionReadSchema)
async def get_all_permission(
        service: PermissionService = Depends(PermissionService)):
    return await service.get_all()


@router.get('/{permission_id}', response_model=PermissionReadSchema)
async def get_permission_or_404(permission_id: str, service: PermissionService = Depends(PermissionService)):
    return await service.get_permission_or_404(permission_id)
