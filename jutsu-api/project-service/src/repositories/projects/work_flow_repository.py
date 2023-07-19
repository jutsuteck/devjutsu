from typing import List
from sqlmodel import Session

from src.models.v1.projects.workflow import Workflow


class WorkflowRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, workflow: Workflow) -> Workflow:
        self.session.add(workflow)
        self.session.commit()
        self.session.refresh(workflow)

        return workflow

    def get_all(self, project_id: str) -> List[Workflow]:
        return self.session.query(Workflow).filter_by(project_id=project_id).all()

    def get_active_workflow(self, project_id):
        return self.session.query(Workflow).filter_by(
            project_id=project_id, is_active=True).first()

    def get(self, workflow_id: str):
        return self.session.query(Workflow).get(workflow_id)

    def update(self, workflow: Workflow, workflow_update_data: dict) -> Workflow:
        for key, value in workflow_update_data.items():
            setattr(workflow, key, value)

        self.session.commit()
        self.session.refresh(workflow)

        return workflow  # type: ignore

    def delete(self, workflow: Workflow) -> None:
        self.session.delete(workflow)
        self.session.commit()
