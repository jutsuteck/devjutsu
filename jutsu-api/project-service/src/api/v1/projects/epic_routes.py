from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.projects.epic_schema import EpicCreateSchema, EpicReadSchema, EpicUpdateSchema
from src.services.projects.epic_service import EpicService


router = APIRouter()


@router.post('/new', response_model=EpicReadSchema)
def epic_create(project_id: str, epic_create_schema: EpicCreateSchema, service: EpicService = Depends(EpicService)):
    return service.create_epic(project_id, epic_create_schema.dict())


@router.get('/all', response_model=List[EpicReadSchema])
def epic_list(project_id: str, service: EpicService = Depends(EpicService)):
    return service.get_all_project_epics(project_id)


@router.get('/{epic_id}', response_model=EpicReadSchema)
def epic_detail(epic_id: str, service: EpicService = Depends(EpicService)):
    return service.get_epic_detail(epic_id)


@router.patch('/update/{epic_id}', response_model=EpicReadSchema)
def epic_update(epic_id: str, epic_update_schema: EpicUpdateSchema, service: EpicService = Depends(EpicService)):
    return service.update_epic(
        epic_id, epic_update_schema.dict(exclude_unset=True))


@router.delete('/delete/{epic_id}')
def epic_delete(epic_id: str, service: EpicService = Depends(EpicService)):
    return service.delete_epic(epic_id)
