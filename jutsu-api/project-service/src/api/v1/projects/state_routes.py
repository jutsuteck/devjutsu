from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.projects.state_schema import StateCreateSchema, StateReadSchema, StateUpdateSchema
from src.services.projects.state_service import StateService


router = APIRouter()


@router.post('/new', response_model=StateReadSchema)
def state_create(workflow_id: str, state_create_schema: StateCreateSchema, service: StateService = Depends(StateService)):
    return service.create_workflow_state(
        workflow_id, state_create_schema.dict())


@router.get('/', response_model=List[StateReadSchema])
def state_list(workflow_id: str, service: StateService = Depends(StateService)):
    return service.get_all_workflow_states(workflow_id)


@router.patch('/update/{state_id}', response_model=StateReadSchema)
def state_update(state_id: str, state_update_schema: StateUpdateSchema, service: StateService = Depends(StateService)):
    return service.update_state(
        state_id, state_update_schema.dict(exclude_unset=True))


@router.delete('/delete/{state_id}')
def state_delete(state_id: str, service: StateService = Depends(StateService)):
    return service.delete_state(state_id)
