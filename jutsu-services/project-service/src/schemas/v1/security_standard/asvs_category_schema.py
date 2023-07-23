from typing import List
from pydantic import BaseModel


class ASVSCategoryReadSchema(BaseModel):
    id: str
    name: str
    objective: str

    sub_categories: List["ASVSSubCategoryReadSchema"] = []

    class Config:
        orm_mode = True


from src.schemas.v1.security_standard.asvs_sub_category_schema import ASVSSubCategoryReadSchema  # noqa
