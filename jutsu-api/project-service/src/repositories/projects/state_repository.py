from typing import List
from sqlmodel import Session
from src.core.exceptions.projects.state_exceptions import StateNotFoundException

from src.models.v1.projects.state import State


class StateRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, state: State) -> State:
        self.session.add(state)
        self.session.commit()
        self.session.refresh(state)

        return state

    def filter_by_workflow(self, workflow_id: str) -> List[State]:
        return self.session.query(State).filter_by(workflow_id=workflow_id).all()

    def get(self, state_id: str) -> State:
        return self.session.query(State).get(state_id)  # type: ignore

    def update(self, state: State, state_update_data: dict) -> State:
        for key, value in state_update_data.items():
            setattr(state, key, value)

        self.session.commit()
        self.session.refresh(state)

        return state

    def delete(self, state: State) -> None:
        self.session.delete(state)
        self.session.commit()
