from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.exceptions.projects.label_exceptions import LabelNotFoundException
from src.models.v1.projects.label import Label
from src.models.v1.projects.work_item import WorkItem
from src.repositories.projects.label_repository import LabelRepository
from src.services.projects.work_item_service import WorkItemService


class LabelService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.label_repository = LabelRepository(self.session)
        self.work_item_service = WorkItemService(self.session)

    def create_work_item_label(self, work_item_id: str, label_data: dict) -> Label:
        work_item = self.work_item_service.get_work_item_or_404(work_item_id)

        label = Label(**label_data)
        label.work_item = work_item

        self.label_repository.add(label)

        return label

    def filter_by_work_item(self, work_item_id: str) -> List[Label]:
        self.work_item_service.get_work_item_or_404(work_item_id)

        return self.label_repository.filter_by_work_item(work_item_id)

    def get_label_or_404(self, label_id: str) -> Label:
        label = self.label_repository.get(label_id)

        if not label:
            raise LabelNotFoundException(label_id)

        return label

    def update_label(self, label_id: str, label_name: str) -> Label:
        label = self.get_label_or_404(label_id)
        label.name = label_name

        self.label_repository.update(label)

        return label

    def delete_label(self, label_id: str) -> None:
        label = self.get_label_or_404(label_id)
        self.label_repository.delete(label)
