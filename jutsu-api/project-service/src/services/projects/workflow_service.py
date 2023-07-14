from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.types.enums import Methodology
from src.core.utils.helpers import generate_workflow_name
from src.models.v1.projects.project import Project
from src.models.v1.projects.workflow import Workflow


class WorkflowService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session

    def create_scrum_workflow(self, project_id: str, workflow_data: dict) -> Workflow:
        project = self.session.query(Project).get(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        if project.methodology != Methodology.SCRUM:
            raise HTTPException(
                status_code=400, detail="Only scrum projects can create new workflows")

        workflow = Workflow(**workflow_data)

        if "name" not in workflow_data:
            workflow.name = generate_workflow_name(project.name_key)

        self.session.add(workflow)
        self.session.commit()
        self.session.refresh(workflow)

        return workflow

    def get_all_project_scrum_workflows(self, project_id: str) -> List[Workflow]:
        project = self.session.query(Project).get(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        if project.methodology != Methodology.SCRUM:
            raise HTTPException(
                status_code=400, detail="Only scrum projects have multiple workflows")

        project_workflows = self.session.query(
            Workflow).filter_by(project_id=project.id).all()

        return project_workflows

    def get_project_active_workflow(self, project_id: str) -> Workflow:
        project = self.session.query(Project).get(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        active_workflow = self.session.query(Workflow).filter_by(
            project_id=project.id, is_active=True).first()

        if not active_workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        return active_workflow

    def update_project_workflow(self, workflow_id: str, workflow_update_data: dict) -> Workflow:
        workflow = self.session.query(Workflow).get(workflow_id)

        if not workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        for key, value in workflow_update_data.items():
            setattr(workflow, key, value)

        self.session.commit()
        self.session.refresh(workflow)

        return workflow

    def delete_workflow(self, workflow_id: str):
        workflow = self.session.query(Workflow).get(workflow_id)

        if not workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        self.session.delete(workflow)
        self.session.commit()

        return workflow
