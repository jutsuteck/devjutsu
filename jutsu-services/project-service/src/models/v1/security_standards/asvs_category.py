import uuid

from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field


class ASVSCategory(SQLModel, table=True):
    __tablename__: str = "asvs_category"

    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: str = Field(unique=True)
    objective: str = Field(...)

    sub_categories: List["ASVSSubCategory"] = Relationship(
        back_populates="asvs_category")


from src.models.v1.security_standards.asvs_sub_category import ASVSSubCategory  # noqa
