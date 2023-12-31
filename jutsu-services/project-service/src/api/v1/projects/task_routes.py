from typing import List
from fastapi import APIRouter, Depends

from src.core.security.auth import get_current_user
from src.schemas.v1.projects.task_schema import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema
from src.services.projects.task_service import TaskService


router = APIRouter(prefix="/api/v1")


@router.post('/tasks/new', response_model=TaskReadSchema)
def task_create(
        work_item_id: str,
        task_create_schema: TaskCreateSchema,
        service: TaskService = Depends(TaskService),
        current_user=Depends(get_current_user)):
    return service.create_task(
        work_item_id, task_create_schema.dict())


@router.get('/tasks/all/{work_item_id}', response_model=List[TaskReadSchema])
def task_list(
        work_item_id: str,
        service: TaskService = Depends(TaskService),
        current_user=Depends(get_current_user)):
    return service.filter_by_work_item(work_item_id)


@router.patch('/tasks/update/{task_id}', response_model=TaskReadSchema)
def task_update(
        task_id: str,
        task_update_schema: TaskUpdateSchema,
        service: TaskService = Depends(TaskService),
        current_user=Depends(get_current_user)):
    return service.update_task(
        task_id, task_update_schema.dict(exclude_unset=True))


@router.delete('/tasks/delete/{task_id}')
def task_delete(
        task_id: str,
        service: TaskService = Depends(TaskService),
        current_user=Depends(get_current_user)):
    return service.delete_task(task_id)
