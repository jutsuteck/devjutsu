from typing import List, Optional
from pydantic import BaseModel

from src.schemas.v1.security_standard.asvs_sub_category_schema import ASVSSubCategoryReadSchema  # noqa


class ASVSCategoryReadSchema(BaseModel):
    id: str
    name: str
    objective: Optional[str]

    sub_categories: List[ASVSSubCategoryReadSchema]

    class Config:
        orm_mode = True
