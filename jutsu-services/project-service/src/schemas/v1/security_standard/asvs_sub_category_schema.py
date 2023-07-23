from typing import List
from pydantic import BaseModel


class ASVSSubCategoryReadSchema(BaseModel):
    id: str
    name: str
    objective: str
    category_id: str

    security_requirements: List["ASVSRequirementReadSchema"] = []

    class Config:
        orm_mode = True
