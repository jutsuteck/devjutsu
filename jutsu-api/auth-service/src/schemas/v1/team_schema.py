from pydantic import BaseModel


class TeamSchema(BaseModel):
    name: str


class TeamCreateSchema(BaseModel):
    name: str
