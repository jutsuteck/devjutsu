import uuid

from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class WorkItemType(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    name: str = Field(...)
    work_items: Optional[List["WorkItem"]] = Relationship(
        back_populates="work_item_type")


from src.models.v1.projects.work_item import WorkItem  # noqa
