from typing import Optional
from pydantic import BaseModel


class CourseCreateSchema(BaseModel):
    title: str
    description: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "",
                "description": ""
            }
        }


class CourseUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]


class CourseReadSchema(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        from_attributes = True
