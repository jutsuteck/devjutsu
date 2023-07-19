from typing import List
from fastapi import Depends
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.exceptions.projects.epic_exceptions import EpicNotFoundException
from src.models.v1.projects.epic import Epic
from src.repositories.projects.epic_repository import EpicRepository
from src.services.projects.project_service import ProjectService


class EpicService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.epic_repository = EpicRepository(self.session)
        self.project_service = ProjectService(self.session)

    def create_epic(self, project_id: str, epic_data: dict) -> Epic:
        self.project_service.get_project_or_404(project_id)

        epic = Epic(**epic_data)

        self.epic_repository.add(epic)

        return epic

    def get_all(self, project_id: str) -> List[Epic]:
        self.project_service.get_project_or_404(project_id)

        epic_list = self.epic_repository.get_all(project_id)

        return epic_list

    def get_epic_or_404(self, epic_id: str) -> Epic:
        epic = self.epic_repository.get(epic_id)

        if not epic:
            raise EpicNotFoundException(epic_id)

        return epic

    def update_epic(self, epic_id: str, epic_update_data: dict) -> Epic:
        epic = self.get_epic_or_404(epic_id)

        return self.epic_repository.update(epic, epic_update_data)

    def delete_epic(self, epic_id: str) -> None:
        epic = self.get_epic_or_404(epic_id)

        self.epic_repository.delete(epic)
