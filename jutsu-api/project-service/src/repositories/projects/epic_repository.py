from typing import List
from sqlmodel import Session
from src.core.exceptions.projects.epic_exceptions import EpicNotFoundException

from src.models.v1.projects.epic import Epic
from src.repositories.projects.project_repository import ProjectRepository


class EpicRepository:
    def __init__(self, session: Session):
        self.session = session
        self.project_repository = ProjectRepository(self.session)

    def add(self, epic: Epic) -> Epic:
        self.session.add(epic)
        self.session.commit()
        self.session.refresh(epic)
        return epic

    def get_all(self, project_id: str) -> List[Epic]:
        return self.session.query(Epic).filter_by(project_id=project_id).all()

    def get(self, epic_id: str):
        return self.session.query(Epic).get(epic_id)

    def update(self, epic: Epic, epic_data: dict) -> Epic:
        for key, value in epic_data.items():
            setattr(epic, key, value)

        self.session.commit()
        self.session.refresh(epic)

        return epic

    def delete(self, epic: Epic) -> None:
        self.session.delete(epic)
        self.session.commit()
