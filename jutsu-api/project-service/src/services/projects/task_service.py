from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.exceptions.projects.task_exceptions import TaskNotFoundException
from src.models.v1.projects.task import Task
from src.models.v1.projects.work_item import WorkItem
from src.repositories.projects.task_repository import TaskRepository
from src.services.projects.work_item_service import WorkItemService


class TaskService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.work_item_service = WorkItemService(self.session)
        self.task_repository = TaskRepository(self.session)

    def create_task(self, work_item_id: str, task_data: dict) -> Task:
        self.work_item_service.get_work_item_or_404(work_item_id)

        task = Task(**task_data)

        self.task_repository.add(task)

        return task

    def filter_by_work_item(self, work_item_id: str) -> List[Task]:
        self.work_item_service.get_work_item_or_404(work_item_id)

        return self.task_repository.filter_by_work_item(work_item_id)

    def get_task_or_404(self, task_id: str) -> Task:
        task = self.task_repository.get(task_id)

        if not task:
            raise TaskNotFoundException(task_id)

        return task

    def update_task(self, task_id: str, task_update_data: dict) -> Task:
        task = self.get_task_or_404(task_id)

        return self.task_repository.update(task, task_update_data)

    def delete_task(self, task_id: str) -> None:
        task = self.get_task_or_404(task_id)

        self.task_repository.delete(task)
