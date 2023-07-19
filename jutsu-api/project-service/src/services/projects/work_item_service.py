from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.exceptions.projects.work_item_exceptions import WorkItemNotFoundException
from src.models.v1.projects.work_item import WorkItem
from src.repositories.projects.work_item_repository import WorkItemRepository
from src.services.projects.state_service import StateService
from src.services.projects.workflow_service import WorkflowService


class WorkItemService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.work_item_repository = WorkItemRepository(self.session)
        self.workflow_service = WorkflowService(self.session)
        self.state_service = StateService(self.session)

    def create_work_item(self, workflow_id: str, state_id: str, work_item_data: dict):
        self.workflow_service.get_workflow_or_404(workflow_id)
        self.state_service.get_state_or_404(state_id)

        work_item = WorkItem(**work_item_data)

        self.work_item_repository.add(work_item)

        return work_item

    def get_all_state_work_items(self, state_id: str) -> List[WorkItem]:
        self.state_service.get_state_or_404(state_id)
        return self.work_item_repository.filter_by_state(state_id)

    def get_work_item_or_404(self, work_item_id: str) -> WorkItem:
        work_item = self.work_item_repository.get(work_item_id)

        if not work_item:
            raise WorkItemNotFoundException(work_item_id)

        return work_item

    def update_work_item_state(self, work_item_id: str, new_state_id: str) -> WorkItem:
        work_item = self.get_work_item_or_404(
            work_item_id)
        self.state_service.get_state_or_404(work_item.state_id)
        self.work_item_repository.update_state(work_item, new_state_id)

        return work_item

    def update_work_item(self, work_item_id: str, work_item_data: dict) -> WorkItem:
        work_item = self.get_work_item_or_404(
            work_item_id)

        return self.work_item_repository.update(work_item, work_item_data)

    def delete_work_item(self, work_item_id: str) -> None:
        work_item = self.get_work_item_or_404(
            work_item_id)

        self.work_item_repository.delete(work_item)
