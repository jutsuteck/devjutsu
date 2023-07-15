from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.projects.epic import Epic
from src.models.v1.projects.project import Project


class EpicService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session

    def create_epic(self, project_id: str, epic_data: dict) -> Epic:
        project = self.session.query(Project).get(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        epic = Epic(**epic_data)

        self.session.add(epic)
        self.session.commit()
        self.session.refresh(epic)

        return epic

    def get_all_project_epics(self, project_id: str) -> List[Epic]:
        project = self.session.query(Project).get(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        project_epics = self.session.query(
            Epic).filter_by(project_id=project.id).all()

        return project_epics

    def get_epic_detail(self, epic_id: str) -> Epic:
        epic = self.session.query(Epic).get(epic_id)

        if not epic:
            raise HTTPException(status_code=404, detail="Epic not found")

        return epic

    def update_epic(self, epic_id: str, epic_update_data: dict) -> Epic:
        epic = self.session.query(Epic).get(epic_id)

        if not epic:
            raise HTTPException(status_code=404, detail="Epic not found")

        for key, value in epic_update_data.items():
            setattr(epic, key, value)

        self.session.commit()
        self.session.refresh(epic)

        return epic

    def delete_epic(self, epic_id: str) -> Epic:
        epic = self.session.query(Epic).get(epic_id)

        if not epic:
            raise HTTPException(status_code=404, detail="Epic not found")

        self.session.delete(epic)
        self.session.commit()

        return epic
