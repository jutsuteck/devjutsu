from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.projects.epic_schema import EpicCreateSchema, EpicReadSchema, EpicUpdateSchema
from src.services.projects.epic_service import EpicService


router = APIRouter()


@router.post('/new', response_model=EpicReadSchema)
def epic_create(project_id: str, epic_create_schema: EpicCreateSchema, service: EpicService = Depends(EpicService)):
    epic = service.create_epic(project_id, epic_create_schema.dict())

    return epic


@router.get('/all', response_model=List[EpicReadSchema])
def epic_list(project_id: str, service: EpicService = Depends(EpicService)):
    project_epics = service.get_all_project_epics(project_id)

    return project_epics


@router.get('/{epic_id}', response_model=EpicReadSchema)
def epic_detail(epic_id: str, service: EpicService = Depends(EpicService)):
    epic = service.get_epic_detail(epic_id)

    return epic


@router.patch('/update/{epic_id}', response_model=EpicReadSchema)
def epic_update(epic_id: str, epic_update_schema: EpicUpdateSchema, service: EpicService = Depends(EpicService)):
    epic = service.update_epic(
        epic_id, epic_update_schema.dict(exclude_unset=True))

    return epic


@router.delete('/delete/{epic_id}', response_model=EpicReadSchema)
def epic_delete(epic_id: str, service: EpicService = Depends(EpicService)):
    epic = service.delete_epic(epic_id)

    return epic
