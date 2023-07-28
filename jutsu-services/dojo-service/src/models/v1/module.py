import uuid

from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from src.models.v1.course import Course


class Module(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    title: str = Field(unique=True)
    description: Optional[str]

    course_id: str = Field(foreign_key="course.id", nullable=False)
    course: Course = Relationship(back_populates="modules")
