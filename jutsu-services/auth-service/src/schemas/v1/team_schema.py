from uuid import UUID
from pydantic import BaseModel


class TeamReadSchema(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True


class TeamCreateSchema(BaseModel):
    name: str


class TeamUpdateSchema(BaseModel):
    name: str
