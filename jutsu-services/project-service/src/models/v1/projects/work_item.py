import uuid

from datetime import datetime
from typing import List, Optional
from sqlmodel import Column, Enum, Field, Relationship, SQLModel

from src.core.types.enums import WorkItemType


class WorkItem(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: str = Field(max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    effort: Optional[int] = Field(default=0)
    ready_for_development: bool = Field(default=False)
    work_item_type: Optional[WorkItemType] = Field(
        default=WorkItemType.USER_STORY, sa_column=Column(Enum(WorkItemType)))

    tasks: Optional[List["Task"]] = Relationship(back_populates="work_item")
    labels: Optional[List["Label"]] = Relationship(back_populates="work_item")

    epic_id: Optional[str] = Field(
        default=None, foreign_key="epic.id", nullable=True)
    epic: Optional["Epic"] = Relationship(back_populates="work_items")

    workflow_id: str = Field(foreign_key="workflow.id", nullable=False)
    workflow: Optional["Workflow"] = Relationship(back_populates="work_items")

    state_id: str = Field(foreign_key="state.id", nullable=False)
    state: Optional["State"] = Relationship(back_populates="work_items")

    created_on: datetime = Field(default_factory=datetime.utcnow)


from src.models.v1.projects.epic import Epic  # noqa
from src.models.v1.projects.label import Label  # noqa
from src.models.v1.projects.state import State  # noqa
from src.models.v1.projects.task import Task  # noqa
from src.models.v1.projects.workflow import Workflow  # noqa
