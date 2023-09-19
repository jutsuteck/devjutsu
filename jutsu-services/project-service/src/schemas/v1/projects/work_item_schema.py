from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator

from src.core.types.enums import WorkItemType
from src.core.utils.helpers import format_datetime
from src.schemas.v1.projects.epic_schema import EpicReadSchema
from src.schemas.v1.projects.label_schema import LabelReadSchema
from src.schemas.v1.projects.state_schema import StateReadSchema
from src.schemas.v1.projects.task_schema import TaskReadSchema
from src.schemas.v1.projects.workflow_schema import WorkflowReadSchema


class WorkItemBaseSchema(BaseModel):
    name: str
    description: Optional[str] = None
    effort: Optional[int] = 0

    workflow_id: str
    state_id: str


class WorkItemCreateSchema(WorkItemBaseSchema):
    ready_for_development: Optional[bool] = False
    work_item_type: Optional[WorkItemType]

    class Config:
        schema_extra = {
            "example": {
                "name": "Auth",
                "description": "As a user I want to login with email and password",
                "effort": 1,
                "ready_for_development": False,
                "work_item_type": "User Story",
                "workflow_id": "{workflow_id}",
                "state_id": "{state_id}"
            }
        }


class WorkItemStateUpdateSchema(BaseModel):
    state_id: str


class WorkItemUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    effort: Optional[int]
    ready_for_development: Optional[bool]
    work_item_type: Optional[WorkItemType]

    state_id: Optional[str]
    epic_id: Optional[str] = None

    @validator('epic_id', pre=True)
    def empty_string_to_none(cls, v):
        return None if v == "" else v


class WorkItemReadSchema(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    effort: int
    ready_for_development: bool
    work_item_type: Optional[WorkItemType] = None
    created_on: datetime

    """ workflow: WorkflowReadSchema """
    """ epic: EpicReadSchema """
    state: StateReadSchema

    labels: List[LabelReadSchema]
    tasks: List[TaskReadSchema]

    class Config:
        orm_mode = True
