import uuid

from typing import Optional
from sqlmodel import Relationship, SQLModel, Field


class ASVSRequirement(SQLModel, table=True):
    __tablename__: str = "asvs_requirement"

    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    requirement_id: str = Field(unique=True)
    description: str = Field(...)
    objective: Optional[str] = Field(default="")
    value: Optional[str] = Field(default="")

    sub_category_id: str = Field(foreign_key="asvs_sub_category.id")
    sub_category: Optional["ASVSSubCategory"] = Relationship(
        back_populates="security_requirement")


from src.models.v1.security_standards.asvs_sub_category import ASVSSubCategory  # noqa
