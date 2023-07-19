from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.projects.task_schema import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema
from src.services.projects.task_service import TaskService


router = APIRouter()


@router.post('/new', response_model=TaskReadSchema)
def task_create(work_item_id: str, task_create_schema: TaskCreateSchema, service: TaskService = Depends(TaskService)):
    return service.create_task(
        work_item_id, task_create_schema.dict())


@router.get('/all/{work_item_id}', response_model=List[TaskReadSchema])
def task_list(work_item_id, service: TaskService = Depends(TaskService)):
    return service.filter_by_work_item(work_item_id)


@router.patch('/update/{task_id}', response_model=TaskReadSchema)
def task_update(task_id: str, task_update_schema: TaskUpdateSchema, service: TaskService = Depends(TaskService)):
    return service.update_task(
        task_id, task_update_schema.dict(exclude_unset=True))


@router.delete('/delete/{task_id}')
def task_delete(task_id: str, service: TaskService = Depends(TaskService)):
    return service.delete_task(task_id)
