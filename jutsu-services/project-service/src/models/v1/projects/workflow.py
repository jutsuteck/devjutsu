import uuid

from datetime import date
from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional


class Workflow(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: Optional[str] = Field(max_length=255, unique=True)
    goal: Optional[str] = Field(max_length=5000, nullable=True)
    is_active: bool = Field(default=False)

    start_date: Optional[date] = Field(nullable=True)
    end_date: Optional[date] = Field(nullable=True)

    project_id: str = Field(foreign_key="project.id", nullable=False)
    project: Optional["Project"] = Relationship(back_populates="workflows")

    states: Optional[List["State"]] = Relationship(
        back_populates="workflow", sa_relationship_kwargs={"cascade": "delete"})

    work_items: Optional[List["WorkItem"]] = Relationship(
        back_populates="workflow")


from src.models.v1.projects.project import Project  # noqa
from src.models.v1.projects.work_item import WorkItem  # noqa
from src.models.v1.projects.state import State  # noqa
