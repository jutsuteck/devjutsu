from typing import Optional
from pydantic import BaseModel


class ModuleCreateSchema(BaseModel):
    title: str
    description: Optional[str]
    course_id: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Introduction to Cybersecurity",
                "description": "",
                "course_id": "{course_id}"
            }
        }


class ModuleUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]


class ModuleReadSchema(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        from_attributes = True
