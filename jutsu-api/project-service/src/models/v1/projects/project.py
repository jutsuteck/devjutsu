import uuid

from datetime import date
from typing import List, Optional
from sqlmodel import Column, Enum, Field, Relationship, SQLModel

from src.core.types.enums import Methodology, SecurityLevel


class Project(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: str = Field(max_length=255, unique=True)
    name_key: Optional[str] = Field(max_length=12, unique=True)
    description: Optional[str] = Field(max_length=500)

    methodology: Methodology = Field(
        default=Methodology.SCRUM, sa_column=Column(Enum(Methodology)))
    security_level: SecurityLevel = Field(
        default=SecurityLevel.LEVEL_1, sa_column=Column(Enum(SecurityLevel)))

    epics: Optional[List["Epic"]] = Relationship(
        back_populates="project", sa_relationship_kwargs={"cascade": "delete"})
    workflows: Optional[List["Workflow"]] = Relationship(
        back_populates="project", sa_relationship_kwargs={"cascade": "delete"})

    created_on: Optional[date] = Field(default=date.today())


from src.models.v1.projects.epic import Epic  # noqa
from src.models.v1.projects.workflow import Workflow  # noqa
