from typing import Optional
from pydantic import BaseModel, validator

from src.types.enums import Methodology, SecurityLevel
from src.utils.helpers import generate_name_key


class ProjectBaseSchema(BaseModel):
    name: str
    name_key: Optional[str]
    description: str
    methodology: Methodology
    security_level: SecurityLevel = SecurityLevel.LEVEL_1


class ProjectCreateSchema(ProjectBaseSchema):

    class Config:
        schema_extra = {
            "example": {
                "name": "Chatterbot",
                "description": "Chatterbot is an engaging AI-driven application that enables real-time, contextually accurate conversations, providing users with a uniquely interactive, personalized experience that adapts and evolves with each interaction.",
                "methodology": "Scrum"
            }
        }

    @validator('name', always=True)
    def set_name_lowercase(cls, name):
        return name.lower()

    @validator('name_key', always=True)
    def set_name_key(cls, name_key, values):
        if name_key is None:
            name = values.get('name', '')
            name_key = generate_name_key(name)
        return name_key


class ProjectUpdateSchema(BaseModel):
    description: Optional[str]
    security_level: Optional[SecurityLevel]


class ProjectDeleteSchema(BaseModel):
    name_key: str


class ProjectReadSchema(ProjectBaseSchema):
    id: str

    class Config:
        orm_mode = True
