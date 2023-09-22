from uuid import UUID
from pydantic import BaseModel


class TenantReadSchema(BaseModel):
    id: UUID
    name: str
