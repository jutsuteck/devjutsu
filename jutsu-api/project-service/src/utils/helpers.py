from datetime import datetime

from sqlmodel import Session

from src.models.v1.projects.project import Project
from src.models.v1.projects.state import State
from src.models.v1.projects.workflow import Workflow
from src.schemas.v1.workflow_schema import WorkflowCreateSchema


def generate_name_key(name: str) -> str:
    words = name.split()
    if len(words) == 1:
        name_key = words[0][:3].upper()
    else:
        name_key = ''.join([word[0] for word in words]).upper()
    return name_key


def generate_workflow_name(project_name_key: str, number: int = 1, name: str = "") -> str:
    current_year = datetime.now().year % 100
    formatted_number = f"{number:02d}"

    if name:
        sanitized_name = '-'.join(name.split())
    else:
        sanitized_name = f'{project_name_key}-{formatted_number}-{current_year}'

    return sanitized_name


def create_default_workflow(project: Project, session: Session):
    workflow_data = WorkflowCreateSchema(
        project_id=project.id, is_active=True)  # type: ignore
    workflow_data.name = generate_workflow_name(
        project.name_key)  # type: ignore

    workflow = Workflow(**workflow_data.dict())
    session.add(workflow)
    session.commit()
    session.refresh(workflow)

    return workflow


def create_default_states(workflow: Workflow, session: Session):
    default_states = [
        {"name": "To Do"},
        {"name": "In Progress"},
        {"name": "In Review"},
        {"name": "Done"}
    ]

    for state_data in default_states:
        state = State(**state_data, workflow=workflow.id)  # type: ignore
        session.add(state)

    session.commit()
