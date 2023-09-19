from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.exceptions.projects.workflow_exceptions import WorklowNotFoundException
from src.core.types.enums import Methodology
from src.core.utils.helpers import generate_workflow_name
from src.models.v1.projects.workflow import Workflow
from src.repositories.projects.work_flow_repository import WorkflowRepository
from src.services.projects.project_service import ProjectService


class WorkflowService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.workflow_repository = WorkflowRepository(self.session)
        self.project_service = ProjectService(self.session)

    def create_workflow(self, workflow_data: dict) -> Workflow:
        project_id = workflow_data["project_id"]

        project = self.project_service.get_project_or_404(project_id)

        if project.methodology != Methodology.SCRUM:
            raise HTTPException(
                status_code=400, detail="Only scrum projects can create new workflows")

        workflow = Workflow(**workflow_data)

        if "name" not in workflow_data:
            workflow.name = generate_workflow_name(
                project.name_key)  # type: ignore

        self.workflow_repository.add(workflow)

        return workflow

    def get_all(self, project_id: str) -> List[Workflow]:
        project = self.project_service.get_project_or_404(project_id)

        workflow_list = self.workflow_repository.get_all(
            project.id)  # type: ignore

        return workflow_list

    def get_workflow_or_404(self, workflow_id: str) -> Workflow:
        workflow = self.workflow_repository.get(workflow_id)

        if not workflow:
            raise WorklowNotFoundException(workflow_id)

        return workflow

    def get_active_workflow(self, project_id: str) -> Workflow:
        project = self.project_service.get_project_or_404(project_id)

        active_workflow = self.workflow_repository.get_active_workflow(
            project_id=project.id)

        if not active_workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        return active_workflow

    def update_workflow(self, workflow_id: str, workflow_update_data: dict) -> Workflow:
        workflow = self.get_workflow_or_404(workflow_id)

        updated_workflow = self.workflow_repository.update(
            workflow, workflow_update_data)  # type: ignore

        return updated_workflow

    def delete_workflow(self, workflow_id: str) -> None:
        workflow = self.get_workflow_or_404(workflow_id)
        self.workflow_repository.delete(workflow)
