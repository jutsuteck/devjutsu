from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.core.exceptions.projects.state_exceptions import StateNotFoundException
from src.models.v1.projects.state import State
from src.models.v1.projects.workflow import Workflow
from src.repositories.projects.state_repository import StateRepository
from src.repositories.projects.work_flow_repository import WorkflowRepository


class StateService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.state_repository = StateRepository(self.session)
        self.workflow_repository = WorkflowRepository(self.session)

    def create_state(self, workflow_id: str, state_data: dict) -> State:
        self.workflow_repository.get_workflow_or_404(workflow_id)

        state = State(**state_data)

        self.state_repository.add(state)

        return state

    def get_all_workflow_states(self, workflow_id: str) -> List[State]:
        workflow = self.workflow_repository.get_workflow_or_404(workflow_id)

        state_list = self.state_repository.filter_by_workflow(
            workflow.id)  # type: ignore

        return state_list

    def get_state_or_404(self, state_id: str) -> State:
        state = self.state_repository.get(state_id)

        if not state:
            raise StateNotFoundException(state_id)

        return state

    def update_state(self, state_id: str, state_update_data: dict) -> State:
        state = self.get_state_or_404(state_id)

        updated_state = self.state_repository.update(state, state_update_data)

        return updated_state

    def delete_state(self, state_id: str) -> None:
        state = self.get_state_or_404(state_id)
        self.state_repository.delete(state)
