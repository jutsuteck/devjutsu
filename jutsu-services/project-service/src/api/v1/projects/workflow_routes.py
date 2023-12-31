from typing import List
from fastapi import APIRouter, Depends

from src.core.security.auth import get_current_user
from src.schemas.v1.projects.workflow_schema import WorkflowCreateSchema, WorkflowReadSchema, WorkflowUpdateSchema
from src.services.projects.workflow_service import WorkflowService


router = APIRouter(prefix="/api/v1")


@router.post('/workflow/new', response_model=WorkflowReadSchema)
def workflow_create(
        workflow_create_schema: WorkflowCreateSchema,
        service: WorkflowService = Depends(WorkflowService),
        current_user=Depends(get_current_user)):
    return service.create_workflow(workflow_create_schema.dict())


@router.get('/workflow/all/{project_id}', response_model=List[WorkflowReadSchema])
def work_flow_list(
        project_id: str,
        service: WorkflowService = Depends(WorkflowService)):
    return service.get_all(project_id)


@router.get('/workflow/current/{project_id}', response_model=WorkflowReadSchema)
def project_active_workflow(
        project_id: str,
        service: WorkflowService = Depends(WorkflowService)):
    return service.get_active_workflow(project_id)


@ router.patch('/workflow/update/{workfow_id}', response_model=WorkflowReadSchema)
def project_workflow_update(
        workflow_id: str,
        workflow_update_schema: WorkflowUpdateSchema,
        service: WorkflowService=Depends(WorkflowService),
        current_user=Depends(get_current_user)):
    return service.update_workflow(
        workflow_id, workflow_update_schema.dict(exclude_unset=True))


@ router.delete('/workflow/delete/{project_id}')
def project_workflow_delete(
        workflow_id: str,
        service: WorkflowService=Depends(WorkflowService),
        current_user=Depends(get_current_user)):
    return service.delete_workflow(workflow_id)
