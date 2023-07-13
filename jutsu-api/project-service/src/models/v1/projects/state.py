import uuid

from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class State(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: str = Field(max_length=255)

    workflow_id: str = Field(foreign_key="workflow.id", nullable=False)
    workflow: Optional["Workflow"] = Relationship(back_populates="states")

    work_items: Optional[List["WorkItem"]
                         ] = Relationship(back_populates="state")


from src.models.v1.projects.work_item import WorkItem  # noqa
from src.models.v1.projects.workflow import Workflow  # noqa
