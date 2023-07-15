from datetime import date, timedelta
from typing import Optional
from pydantic import BaseModel, validator


class EpicBaseSchema(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    project_id: str

    @validator('end_date', pre=True)
    def emptr_str_none(cls, v):
        return None if v == "" else v


class EpicCreateSchema(EpicBaseSchema):

    class Config:
        schema_extra = {
            "example": {
                "name": "Epic 1",
                "description": "Some description",
                "start_date": date.today().isoformat(),
                "end_date": (date.today() + timedelta(days=90)).isoformat(),
                "project_id": "{project_id}"
            }
        }


class EpicUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class EpicReadSchema(BaseModel):
    id: str
    description: str
    start_date: date
    end_date: date

    class Config:
        orm_mode = True
