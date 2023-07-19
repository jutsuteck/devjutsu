from typing import List
from sqlmodel import Session

from src.models.v1.projects.label import Label


class LabelRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, label: Label) -> Label:
        self.session.add(label)
        self.session.commit()
        return label

    def filter_by_work_item(self, work_item_id: str) -> List[Label]:
        return self.session.query(Label).filter_by(work_item_id=work_item_id).all()

    def get(self, label_id: str) -> Label | None:
        return self.session.query(Label).get(label_id)

    def update(self, label: Label) -> None:
        self.session.commit()
        self.session.refresh(label)

    def delete(self, label: Label) -> None:
        self.session.delete(label)
        self.session.commit()
