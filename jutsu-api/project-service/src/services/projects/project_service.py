from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session
from src.core.dependencies.database.database_manager import db_session

from src.core.utils.helpers import generate_workflow_name
from src.models.v1.projects.project import Project
from src.models.v1.projects.state import State
from src.models.v1.projects.workflow import Workflow
from src.schemas.v1.projects.workflow_schema import WorkflowCreateSchema


class ProjectService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session

    def create_project(self, project_data: dict) -> Project:
        project = Project(**project_data)

        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)

        workflow = self.create_default_project_workflow(project)
        self.create_default_workflow_states(workflow)

        return project

    def get_all_projects(self) -> List[Project]:
        return self.session.query(Project).all()

    def update_project(self, project_id: str, project_update_data: dict) -> Project:
        project: Project = self.session.query(
            Project).get(project_id)  # type: ignore

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        for key, value in project_update_data.items():
            setattr(project, key, value)

        self.session.commit()
        self.session.refresh(project)

        return project

    def delete_project(self, project_id: str, name_key: str) -> Project:
        project: Project = self.session.query(
            Project).get(project_id)  # type: ignore

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        if project.name_key != name_key:
            raise HTTPException(status_code=404, detail="Incorrect name key")

        self.session.delete(project)
        self.session.commit()

        return project

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
