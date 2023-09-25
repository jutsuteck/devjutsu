import uuid

from typing import Optional
from fastapi_users import schemas

from src.schemas.v1.tenant_schemas import TenantReadSchema


class MemberCreateSchema(schemas.BaseUserCreate):
    pass


class MemberReadSchema(schemas.BaseUser[uuid.UUID]):
    name: Optional[str]
    is_onboarded: bool
    tenant: Optional[TenantReadSchema]


class MemberUpdateSchema(schemas.BaseUserUpdate):
    name: Optional[str] = None
    is_onboarded: Optional[bool] = None
