from datetime import date
from typing import Optional
from pydantic import BaseModel


class EpicBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    project_id: str


class EpicCreateSchema(EpicBaseSchema):

    class Config:
        schema_extra = {
            "example": {
                "name": "Epic 1",
                "description": "Some description",
                "start_date": date.today().isoformat(),
                "end_date": "",
            }
        }


class EpicReadSchema(EpicBaseSchema):
    id: str

    class Config:
        orm_mode = True
