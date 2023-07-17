from typing import List
from sqlmodel import Session
from src.core.exceptions.projects.project_exceptions import ProjectNotFoundException

from src.models.v1.projects.project import Project


class ProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, project: Project) -> Project:
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)

        return project

    def get_all(self) -> List[Project]:
        return self.session.query(Project).all()

    def get_project_or_404(self, project_id: str) -> Project:
        project = self.session.query(Project).get(project_id)

        if not project:
            raise ProjectNotFoundException(project_id)

        return project

    def update(self, project: Project, project_update_data: dict) -> Project:
        for key, value in project_update_data.items():
            setattr(project, key, value)

        self.session.commit()
        self.session.refresh(project)

        return project

    def delete(self, project: Project) -> None:
        self.session.delete(project)
        self.session.commit()
