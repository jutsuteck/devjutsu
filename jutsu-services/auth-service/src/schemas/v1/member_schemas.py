from typing import Optional
import uuid

from fastapi_users import schemas

from src.models.v1.users import Tenant
from src.schemas.v1.tenant_schemas import TenantReadSchema


class MemberReadSchema(schemas.BaseUser[uuid.UUID]):
    first_name: Optional[str]
    last_name: Optional[str]
    tenant: Optional[TenantReadSchema]


class MemberCreateSchema(schemas.BaseUserCreate):

    class Config:
        json_schema_extra = {
            "example": {
                "email": "clarkkent@email.com",
                "password": "iamavalidpassword"
            }
        }


class MemberUpdateSchema(schemas.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]
