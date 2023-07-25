from pydantic import BaseModel
from uuid import UUID


class RoleCreateSchema(BaseModel):
    name: str


class RoleUpdateSchema(BaseModel):
    name: str


class RoleReadSchema(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True
