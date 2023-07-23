import uuid

from typing import Optional
from sqlmodel import Field, Relationship, SQLModel


class Task(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    description: str = Field(max_length=255)
    completed: bool = Field(default=False)

    work_item_id: str = Field(foreign_key="workitem.id", nullable=False)
    work_item: Optional["WorkItem"] = Relationship(back_populates="tasks")


from src.models.v1.projects.work_item import WorkItem  # noqa
