from datetime import date, timedelta
from typing import Optional
from pydantic import BaseModel


class WorkflowBaseSchema(BaseModel):
    project_id: str
    name: Optional[str] = None
    goal: Optional[str] = None
    is_active: Optional[bool] = False
    start_date: Optional[date] = date.today()
    end_date: Optional[date] = None


class WorkflowCreateSchema(WorkflowBaseSchema):

    class Config:
        schema_extra = {
            "example": {
                "project_id": "{project_id}",
                "name": "Workflow name",
                "goal": "Deliver amazing things",
                "start_date": date.today().isoformat(),
                "end_date": (date.today() + timedelta(weeks=3)).isoformat()
            }
        }


class WorkflowUpdateSchema(BaseModel):
    name: Optional[str] = None
    goal: Optional[str] = None
    is_active: Optional[bool]
    start_date: Optional[date] = date.today()
    end_date: Optional[date] = None


class WorkflowReadSchema(WorkflowBaseSchema):
    id: str

    class Config:
        orm_mode = True
