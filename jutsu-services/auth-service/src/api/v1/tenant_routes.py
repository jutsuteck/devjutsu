from fastapi import APIRouter, Depends

from src.services.tenant_schemas import TenantCreateSchema, TenantReadSchema
from src.services.tenant_service import TenantService


router = APIRouter()


@router.post('/new', response_model=TenantReadSchema)
async def create_tenant(
        tenant_create_schema: TenantCreateSchema,
        service: TenantService = Depends(TenantService)):
    return await service.create_tenant(tenant_create_schema.model_dump())


@router.get('/{tenant_id}', response_model=TenantReadSchema)
async def get_tenant(
        tenant_id: str,
        service: TenantService = Depends(TenantService)):
    return await service.get_tenant_or_404(tenant_id)


@router.delete('/delete/{tenant_id}')
async def delete_tenant(
        tenant_id: str,
        service: TenantService = Depends(TenantService)):
    return await service.delete_tenant(tenant_id)
