import uuid

from typing import Optional
from sqlmodel import Field, SQLModel


class Course(SQLModel, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(
        uuid.uuid4()), primary_key=True, nullable=False)
    title: str = Field(max_length=255, unique=True)
    description: Optional[str] = Field(max_length=500)
    target_audience: str = Field(...)
