from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.projects.work_item_schema import WorkItemCreateSchema, WorkItemReadSchema, WorkItemStateUpdateSchema, WorkItemUpdateSchema
from src.services.projects.work_item_service import WorkItemService


router = APIRouter()


@router.post('/new', response_model=WorkItemReadSchema)
def work_item_create(workflow_id: str, state_id: str, work_item_create_schema: WorkItemCreateSchema, service: WorkItemService = Depends(WorkItemService)):
    return service.create_work_item(
        workflow_id, state_id, work_item_create_schema.dict())


@router.get('/state/{state_id}', response_model=List[WorkItemReadSchema])
def state_work_items(state_id: str, service: WorkItemService = Depends(WorkItemService)):
    return service.get_all_state_work_items(state_id)


@router.get('/{work_item_id}', response_model=WorkItemReadSchema)
def work_item_detail(work_item_id: str, service: WorkItemService = Depends(WorkItemService)):
    return service.get_work_item_detail(work_item_id)


@router.patch('/update_state/{work_item_id}', response_model=WorkItemReadSchema)
def work_item_state_update(work_item_id: str, work_item_state_update_schema: WorkItemStateUpdateSchema, service: WorkItemService = Depends(WorkItemService)):
    return service.update_work_item_state(
        work_item_id, work_item_state_update_schema.state_id)


@router.patch('/update/{work_item_id}', response_model=WorkItemReadSchema)
def work_item_update(work_item_id, work_item_update_schema: WorkItemUpdateSchema, service: WorkItemService = Depends(WorkItemService)):
    return service.update_work_item(
        work_item_id, work_item_update_schema.dict(exclude_unset=True))


@router.delete('/delete/{work_item_id}')
def work_item_delete(work_item_id, service: WorkItemService = Depends(WorkItemService)):
    return service.delete_work_item(work_item_id)
