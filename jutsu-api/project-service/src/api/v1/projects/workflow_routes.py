from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.projects.workflow_schema import WorkflowCreateSchema, WorkflowReadSchema, WorkflowUpdateSchema
from src.services.projects.workflow_service import WorkflowService


router = APIRouter()


@router.post('/new', response_model=WorkflowReadSchema)
def project_scrum_workflow_create(project_id: str, workflow_create_schema: WorkflowCreateSchema, service: WorkflowService = Depends(WorkflowService)):
    workflow = service.create_scrum_workflow(
        project_id, workflow_create_schema.dict())

    return workflow


@router.get('/all', response_model=List[WorkflowReadSchema])
def project_scrum_workflows(project_id: str, service: WorkflowService = Depends(WorkflowService)):
    project_workflows = service.get_all_project_scrum_workflows(project_id)

    return project_workflows


@router.get('/current', response_model=WorkflowReadSchema)
def project_active_workflow(project_id: str, service: WorkflowService = Depends(WorkflowService)):
    active_workflow = service.get_project_active_workflow(project_id)

    return active_workflow


@router.patch('/update/{workfow_id}', response_model=WorkflowReadSchema)
def project_workflow_update(workflow_id: str, workflow_update_schema: WorkflowUpdateSchema, service: WorkflowService = Depends(WorkflowService)):
    workflow = service.update_project_workflow(
        workflow_id, workflow_update_schema.dict(exclude_unset=True))

    return workflow


@router.delete('/delete/{project_id}', response_model=WorkflowReadSchema)
def project_workflow_delete(workflow_id: str, service: WorkflowService = Depends(WorkflowService)):
    workflow = service.delete_workflow(workflow_id)

    return workflow
