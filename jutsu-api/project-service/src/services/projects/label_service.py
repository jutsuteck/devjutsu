from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.projects.label import Label
from src.models.v1.projects.work_item import WorkItem


class LabelService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session

    def create_work_item_label(self, work_item_id: str, label_data: dict) -> Label:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        label = Label(**label_data)
        label.work_item = work_item

        self.session.add(label)
        self.session.commit()
        self.session.refresh(label)

        return label

    def get_all_work_item_labels(self, work_item_id: str) -> List[Label]:
        work_item = self.session.query(WorkItem).get(work_item_id)

        if not work_item:
            raise HTTPException(status_code=404, detail="Work item not found")

        work_item_labels = self.session.query(
            Label).filter_by(work_item_id=work_item.id).all()

        return work_item_labels

    def update_label(self, label_id: str, label_name: str) -> Label:
        label: Label = self.session.query(Label).get(label_id)  # type: ignore

        if not label:
            raise HTTPException(status_code=404, detail="Label not found")

        label.name = label_name

        self.session.commit()
        self.session.refresh(label)

        return label

    def delete_label(self, label_id: str) -> None:
        label = self.session.query(Label).get(label_id)

        if not label:
            raise HTTPException(status_code=404, detail="Label not found")

        self.session.delete(label)
        self.session.commit()
