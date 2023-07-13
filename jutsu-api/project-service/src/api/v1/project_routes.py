import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from src.models.v1.projects.project import Project
from src.schemas.v1.project_schema import ProjectCreateSchema, ProjectDeleteSchema, ProjectReadSchema, ProjectUpdateSchema
from src.utils.database import db_session
from src.utils.helpers import create_default_states, create_default_workflow


router = APIRouter()


@router.post('/new', response_model=ProjectReadSchema)
def project_create(project: ProjectCreateSchema, session: Session = Depends(db_session)):
    """
    Create a new project in the database.

    This endpoint accepts a POST request with a body that should conform to the ProjectCreateSchema.
    The function creates a new Project instance with a unique ID and properties specified in the request body.
    The new project is added to the database session, which is then committed to persist the changes.
    The session is refreshed to ensure the new project reflects the current state in the database.
    The newly created project is returned as a response.

    Args:
        project (ProjectCreateSchema): a Pydantic model instance containing the data for the new project.
        session (Session, optional): SQLAlchemy Session for interacting with the database. 
            If not supplied, a session is automatically provided by the db_session dependency.

    Returns:
        ProjectReadSchema: a Pydantic model instance representing the newly created project.
    """
    project_new = Project(id=str(uuid.uuid4()), **project.dict())

    session.add(project_new)
    session.commit()
    session.refresh(project_new)

    workflow = create_default_workflow(project_new, session)
    """ create_default_states(workflow, session) """

    return project_new


@router.post('/', response_model=List[ProjectReadSchema])
def project_list(session: Session = Depends(db_session)):
    """
    Retrieve a list of all projects from the database.

    This endpoint accepts a POST request and returns a list of all projects in the database. 
    Each project in the list conforms to the ProjectReadSchema. The projects are fetched by executing 
    a SELECT ALL operation on the Project table in the database via the session query.

    Args:
        session (Session, optional): SQLAlchemy Session for interacting with the database. 
            If not supplied, a session is automatically provided by the db_session dependency.

    Returns:
        List[ProjectReadSchema]: A list of Pydantic model instances each representing a project in the database.
    """
    return session.query(Project).all()


@router.patch('/patch/{project_id}', response_model=ProjectReadSchema)
def project_update(project_id: str, project_update_schema: ProjectUpdateSchema, session: Session = Depends(db_session)):
    """
    Update a specific project in the database.

    This endpoint accepts a PATCH request with a JSON payload conforming to ProjectUpdateSchema, 
    and updates the corresponding project record in the database identified by the provided project_id. 
    Only the fields provided in the payload will be updated, all others will be left unchanged.

    If the project_id does not correspond to an existing project, a 404 HTTPException is raised.

    Args:
        project_id (str): The ID of the project to be updated.
        project (ProjectUpdateSchema): Pydantic model instance containing the updated field values.
        session (Session, optional): SQLAlchemy Session for interacting with the database. 
            If not supplied, a session is automatically provided by the db_session dependency.

    Returns:
        ProjectReadSchema: A Pydantic model instance representing the updated project.
    """
    project = session.query(Project).get(project_id)  # type: ignore

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    update_data = project_update_schema.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(project, key, value)

    session.commit()
    session.refresh(project)

    return project


@router.delete('/delete/{project_id}', response_model=ProjectReadSchema)
def project_delete(project_id: str, project_delete_schema: ProjectDeleteSchema, session: Session = Depends(db_session)):
    """
    Delete a specific project in the database.

    This endpoint accepts a DELETE request with a JSON payload containing the unique project 'name_key'. 
    It checks if the provided 'name_key' matches with the one in the database. If it matches, the corresponding 
    project identified by the project_id is deleted from the database.

    If the project_id does not correspond to an existing project, or the 'name_key' does not match, 
    a 404 HTTPException is raised.

    Args:
        project_id (str): The ID of the project to be deleted.
        project_key (ProjectKeySchema): Pydantic model instance containing the 'name_key' of the project to be deleted.
        session (Session, optional): SQLAlchemy Session for interacting with the database. 
            If not supplied, a session is automatically provided by the db_session dependency.

    Returns:
        ProjectReadSchema: A Pydantic model instance representing the deleted project.
    """
    project = session.query(Project).get(project_id)  # type: ignore

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.name_key != project_delete_schema.name_key:
        raise HTTPException(status_code=400, detail="Incorrect name key")

    session.delete(project)
    session.commit()

    return project
