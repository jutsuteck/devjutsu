from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.models.v1.projects.project import Project
from src.models.v1.projects.workflow import Workflow
from src.schemas.v1.workflow_schema import WorkflowCreateSchema, WorkflowReadSchema
from src.types.enums import Methodology
from src.utils.database import db_session


router = APIRouter()


@router.post('/new', response_model=WorkflowReadSchema)
def project_scrum_workflow_create(project_id: str, workflow: WorkflowCreateSchema, session: Session = Depends(db_session)):
    project = session.query(Project).get(project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.methodology != Methodology.SCRUM:
        raise HTTPException(
            status_code=403, detail="Method not allowed for non-scrum projects")

    workflow_new = Workflow(id=str(uuid.uuid4()), **workflow.dict())

    session.add(workflow_new)
    session.refresh(workflow_new)

    return workflow_new


@router.get('/all', response_model=List[WorkflowReadSchema])
def project_scrum_workflows(project_id: str, session: Session = Depends(db_session)):
    project = session.query(Project).get(project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.methodology != Methodology.SCRUM:
        raise HTTPException(
            status_code=403, detail="Method not allowed for not-scrum projects")

    project_workflows = session.query(
        Workflow).filter_by(project_id=project.id).all()

    return project_workflows


@router.get('/current', response_model=WorkflowReadSchema)
def project_active_workflow(project_id: str, session: Session = Depends(db_session)):
    project = session.query(Project).get(project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    workflow = session.query(Workflow).filter_by(
        project_id=project.id, is_active=True).first()

    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")

    return workflow
