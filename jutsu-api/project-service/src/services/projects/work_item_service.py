from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.projects.state import State
from src.models.v1.projects.work_item import WorkItem
from src.models.v1.projects.workflow import Workflow


class WorkItemService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session

    def create_work_item(self, workflow_id: str, state_id: str, work_item_data: dict):
        workflow = self.session.query(Workflow).get(workflow_id)

        if not workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        state = self.session.query(State).get(state_id)

        if not state:
            raise HTTPException(status_code=404, detail="State not found")

        work_item = WorkItem(**work_item_data)

        self.session.add(work_item)
        self.session.commit()
        self.session.refresh(work_item)

        return work_item

    def get_all_state_work_items(self, state_id: str) -> List[WorkItem]:
        state = self.session.query(State).get(state_id)

        if not state:
            raise HTTPException(status_code=404, detail="State not found")

        state_work_items = self.session.query(
            WorkItem).filter_by(state_id=state.id).all()

        return state_work_items

    def get_work_item_detail(self, work_item_id: str) -> WorkItem:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        return work_item

    def update_work_item_state(self, work_item_id: str, new_state_id: str) -> WorkItem:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        state = self.session.query(State).get(new_state_id)

        if not state:
            raise HTTPException(status_code=404, detail="State not found")

        work_item.state_id = state.id

        self.session.commit()
        self.session.refresh(work_item)

        return work_item

    def update_work_item(self, work_item_id: str, work_item_data: dict) -> WorkItem:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        for key, value in work_item_data.items():
            setattr(work_item, key, value)

        self.session.commit()
        self.session.refresh(work_item)

        return work_item

    def delete_work_item(self, work_item_id: str) -> None:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        self.session.delete(work_item)
        self.session.commit()
