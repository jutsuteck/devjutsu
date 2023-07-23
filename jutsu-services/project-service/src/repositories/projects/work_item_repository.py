from typing import List
from sqlmodel import Session

from src.models.v1.projects.work_item import WorkItem


class WorkItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, work_item: WorkItem) -> WorkItem:
        self.session.add(work_item)
        self.session.commit()
        self.session.refresh(work_item)

        return work_item

    def filter_by_state(self, state_id: str) -> List[WorkItem]:
        return self.session.query(WorkItem).filter_by(state_id=state_id).all()

    def get(self, work_item_id: str) -> WorkItem:
        return self.session.query(WorkItem).get(work_item_id)  # type: ignore

    def update(self, work_item: WorkItem, work_item_data: dict) -> WorkItem:
        for key, value in work_item_data.items():
            setattr(work_item, key, value)

        self.session.commit()
        self.session.refresh(work_item)

        return work_item

    def update_state(self, work_item: WorkItem, new_state_id: str) -> WorkItem:
        work_item.state_id = new_state_id

        self.session.commit()
        self.session.refresh(work_item)

        return work_item

    def delete(self, work_item: WorkItem) -> None:
        self.session.delete(work_item)
        self.session.commit()
