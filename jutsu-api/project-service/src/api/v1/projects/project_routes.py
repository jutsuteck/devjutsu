from fastapi import APIRouter, Depends
from typing import List

from src.schemas.v1.projects.project_schema import ProjectCreateSchema, ProjectDeleteSchema, ProjectReadSchema, ProjectUpdateSchema
from src.services.projects.project_service import ProjectService


router = APIRouter()


@router.post('/new', response_model=ProjectReadSchema)
def project_create(project_create_schema: ProjectCreateSchema, service: ProjectService = Depends(ProjectService)):
    return service.create_project(project_create_schema.dict())


@router.get('/', response_model=List[ProjectReadSchema])
def project_list(service: ProjectService = Depends(ProjectService)):
    return service.get_all_projects()


@router.patch('/patch/{project_id}', response_model=ProjectReadSchema)
def project_update(project_id: str, project_update_schema: ProjectUpdateSchema, service: ProjectService = Depends(ProjectService)):
    return service.update_project(
        project_id, project_update_schema.dict(exclude_unset=True))


@router.delete('/delete/{project_id}', response_model=ProjectReadSchema)
def project_delete(project_id: str, project_delete_schema: ProjectDeleteSchema, service: ProjectService = Depends(ProjectService)):
    return service.delete_project(
        project_id, project_delete_schema.name_key)
