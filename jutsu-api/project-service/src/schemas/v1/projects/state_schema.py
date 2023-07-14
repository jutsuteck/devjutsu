from typing import List
from pydantic import BaseModel


class StateCreateSchema(BaseModel):
    name: str
    workflow_id: str

    class Config:
        schema_extra = {
            "example": {
                "name": "To Do",
                "workflow_id": ""
            }
        }


class StateUpdateSchema(BaseModel):
    name: str


class StateReadSchema(BaseModel):
    id: str
    name: str
