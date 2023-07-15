from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.projects.task import Task
from src.models.v1.projects.work_item import WorkItem


class TaskService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session

    def create_work_item_task(self, work_item_id: str, task_data: dict) -> Task:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        task = Task(**task_data)

        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)

        return task

    def get_all_work_item_tasks(self, work_item_id: str) -> List[Task]:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        work_item_tasks = self.session.query(
            Task).filter_by(work_item_id=work_item.id).all()

        return work_item_tasks

    def update_task(self, task_id: str, task_update_data: dict) -> Task:
        task = self.session.query(Task).get(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        for key, value in task_update_data.items():
            setattr(task, key, value)

        return task

    def delete_task(self, task_id: str) -> None:
        task = self.session.query(Task).get(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        self.session.delete(task)
        self.session.commit()
