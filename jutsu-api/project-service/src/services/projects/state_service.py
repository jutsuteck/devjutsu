from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.projects.state import State
from src.models.v1.projects.workflow import Workflow


class StateService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session

    def create_workflow_state(self, workflow_id: str, state_data: dict) -> State:
        workflow = self.session.query(Workflow).get(workflow_id)

        if not workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        state = State(**state_data)

        self.session.add(state)
        self.session.commit()
        self.session.refresh(state)

        return state

    def get_all_workflow_states(self, workflow_id: str) -> List[State]:
        workflow = self.session.query(Workflow).get(workflow_id)

        if not workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        workflow_states = self.session.query(
            State).filter_by(workflow_id=workflow.id).all()

        return workflow_states

    def update_state(self, state_id: str, state_update_data: dict) -> State:
        state = self.session.query(State).get(state_id)

        if not state:
            raise HTTPException(status_code=404, detail="State not found")

        for key, value in state_update_data.items():
            setattr(state, key, value)

        self.session.commit()
        self.session.refresh(state)

        return state

    def delete_state(self, state_id: str) -> State:
        state = self.session.query(State).get(state_id)

        if not state:
            raise HTTPException(status_code=404, detail="State not found")

        self.session.delete(state)
        self.session.commit()

        return state
