import uuid

from datetime import date
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class Epic(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: str = Field(nullable=False, max_length=255)
    description: Optional[str] = Field(nullable=False, max_length=255)

    project_id: str = Field(foreign_key="project.id", nullable=False)
    project: Optional["Project"] = Relationship(back_populates="epics")

    work_items: Optional[List["WorkItem"]
                         ] = Relationship(back_populates="epic")

    start_date: Optional[date] = Field(default=date.today())
    end_date: Optional[date] = Field(nullable=True)


from src.models.v1.projects.project import Project  # noqa
from src.models.v1.projects.work_item import WorkItem  # noqa
