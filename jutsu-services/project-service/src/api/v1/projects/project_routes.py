from fastapi import APIRouter, Depends, Request
from typing import List
from src.core.security.auth import get_current_user

from src.schemas.v1.projects.project_schema import ProjectCreateSchema, ProjectDeleteSchema, ProjectReadSchema, ProjectUpdateSchema
from src.services.projects.project_service import ProjectService


router = APIRouter(prefix="/api/v1")


@router.post('/projects/new', response_model=ProjectReadSchema)
def project_create(
        project_create_schema: ProjectCreateSchema,
        service: ProjectService = Depends(ProjectService)):
    return service.create_project(project_create_schema.dict())


@router.get('/projects', response_model=List[ProjectReadSchema])
def project_list(
        service: ProjectService = Depends(ProjectService),
        current_user=Depends(get_current_user)):

    return service.get_all_projects()


@router.get('/projects/{project_id}', response_model=ProjectReadSchema)
def project_detail(project_id: str, service: ProjectService = Depends(ProjectService), current_user=Depends(get_current_user)):
    return service.get_project_or_404(project_id)


@ router.patch('/projects/patch/{project_id}', response_model=ProjectReadSchema)
def project_update(
        project_id: str,
        project_update_schema: ProjectUpdateSchema,
        service: ProjectService = Depends(ProjectService),
        current_user=Depends(get_current_user)):
    return service.update_project(
        project_id, project_update_schema.dict(exclude_unset=True))


@ router.delete('/projects/delete/{project_id}')
def project_delete(
        project_id: str,
        project_delete_schema: ProjectDeleteSchema,
        service: ProjectService = Depends(ProjectService),
        current_user=Depends(get_current_user)):
    return service.delete_project(
        project_id, project_delete_schema.name_key)
