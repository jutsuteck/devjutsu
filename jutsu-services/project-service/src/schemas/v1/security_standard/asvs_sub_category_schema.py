from typing import List
from pydantic import BaseModel

from src.schemas.v1.security_standard.asvs_requirement_schema import ASVSRequirementReadSchema


class ASVSSubCategoryReadSchema(BaseModel):
    id: str
    name: str
    objective: str
    category_id: str

    security_requirements: List[ASVSRequirementReadSchema]

    class Config:
        orm_mode = True
