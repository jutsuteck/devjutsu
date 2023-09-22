from uuid import UUID
from pydantic import BaseModel


class ClanReadSchema(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True


class ClanCreateSchema(BaseModel):
    name: str


class ClanUpdateSchema(BaseModel):
    name: str
