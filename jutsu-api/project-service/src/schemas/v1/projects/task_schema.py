from typing import Optional
from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    description: str
    work_item_id: str

    class Config:
        schema_extra = {
            "example": {
                "description": "Task 1",
                "work_item_id": "{work_item_id}"
            }
        }


class TaskUpdateSchema(BaseModel):
    description: Optional[str] = None
    completed: Optional[bool] = False


class TaskReadSchema(BaseModel):
    id: str
    description: str

    completed: bool
    work_item_id: str

    class Config:
        orm_mode = True
