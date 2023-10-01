import uuid

from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field


class ASVSSubCategory(SQLModel, table=True):
    __tablename__: str = "asvs_sub_category"

    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: str = Field(unique=True)
    objective: Optional[str] = Field(...)

    category_id: str = Field(foreign_key="asvs_category.id")
    category: Optional["ASVSCategory"] = Relationship(
        back_populates="sub_categories")

    security_requirements: List["ASVSRequirement"] = Relationship(
        back_populates="sub_category")


from src.models.v1.security_standards.asvs_requirement import ASVSRequirement  # noqa
from src.models.v1.security_standards.asvs_category import ASVSCategory  # noqa
