from typing import List, Optional
from sqlmodel import Session

from src.models.v1.projects.task import Task


class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, task: Task) -> Task:
        self.session.add(task)
        self.session.commit()

        return task

    def filter_by_work_item(self, work_item_id: str) -> List[Task]:
        return self.session.query(Task).filter_by(work_item_id=work_item_id).all()

    def get(self, task_id: str) -> Task | None:
        return self.session.query(Task).get(task_id)

    def update(self, task: Task, task_data: dict) -> Task:
        for key, value in task_data.items():
            setattr(task, key, value)

        self.session.commit()
        self.session.refresh(task)

        return task

    def delete(self, task: Task) -> None:
        self.session.delete(task)
        self.session.commit()
