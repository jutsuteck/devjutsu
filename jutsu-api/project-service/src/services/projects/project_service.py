from typing import List
from fastapi import Depends
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.exceptions.projects.project_exceptions import IncorrectProjectNameKeyException
from src.core.utils.helpers import generate_workflow_name
from src.models.v1.projects.project import Project
from src.models.v1.projects.state import State
from src.models.v1.projects.workflow import Workflow
from src.repositories.projects.project_repository import ProjectRepository
from src.schemas.v1.projects.workflow_schema import WorkflowCreateSchema


class ProjectService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.project_repository = ProjectRepository(self.session)

    def create_project(self, project_data: dict) -> Project:
        project = Project(**project_data)

        self.project_repository.create(project)

        workflow = self.create_default_project_workflow(project)
        self.create_default_workflow_states(workflow)

        return project

    def get_all_projects(self) -> List[Project]:
        return self.project_repository.get_all()

    def update_project(self, project_id: str, project_update_data: dict) -> Project:
        project = self.project_repository.get_project_or_404(project_id)

        updated_project = self.project_repository.update(
            project, project_update_data)

        return updated_project

    def delete_project(self, project_id: str, name_key: str) -> None:
        project = self.project_repository.get_project_or_404(project_id)

        if project.name_key != name_key:
            raise IncorrectProjectNameKeyException(project.name_key)

        self.project_repository.delete(project)

    def create_default_project_workflow(self, project: Project) -> Workflow:
        workflow_data = WorkflowCreateSchema(
            project_id=project.id, is_active=True)  # type: ignore
        workflow_data.name = generate_workflow_name(
            project.name_key)  # type: ignore

        workflow = Workflow(**workflow_data.dict())
        self.session.add(workflow)
        self.session.commit()
        self.session.refresh(workflow)

        return workflow

    def create_default_workflow_states(self, workflow: Workflow) -> None:
        default_states = [
            {"name": "To Do"},
            {"name": "In Progress"},
            {"name": "In Review"},
            {"name": "Done"}
        ]

        for state_data in default_states:
            state = State(
                **state_data, workflow_id=workflow.id)  # type: ignore
            self.session.add(state)

        self.session.commit()
