import pytest

from unittest.mock import Mock
from sqlmodel import Session
from src.core.exceptions.projects.workflow_exceptions import WorklowNotFoundException

from src.models.v1.projects.workflow import Workflow
from src.repositories.projects.work_flow_repository import WorkflowRepository


@pytest.fixture
def mock_session():
    return Mock(spec=Session)


@pytest.fixture
def workflow_repository(mock_session):
    return WorkflowRepository(mock_session)


def test_workflow_repository_add(workflow_repository: WorkflowRepository, mock_session):
    mock_workflow = Mock(spec=Workflow)

    workflow_repository.add(mock_workflow)

    mock_session.add.assert_called_once_with(mock_workflow)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(mock_workflow)


def test_workflow_repository_get_all(workflow_repository: WorkflowRepository, mock_session):
    mock_project_id = "mock-project-id"
    mock_workflows = [Mock(spec=Workflow), Mock(spec=Workflow)]

    mock_query = mock_session.query.return_value
    mock_filtered_query = mock_query.filter_by.return_value
    mock_filtered_query.all.return_value = mock_workflows

    workflows = workflow_repository.get_all(mock_project_id)

    mock_session.query.assert_called_once_with(Workflow)
    mock_query.filter_by.assert_called_once_with(project_id=mock_project_id)
    assert workflows == mock_workflows


def test_workflow_repository_get(workflow_repository: WorkflowRepository, mock_session):
    mock_workflow_id = "mock-workflow-id"
    mock_workflow = Mock(speck=Workflow)

    mock_query = mock_session.query.return_value
    mock_query.get.return_value = mock_workflow

    workflow = workflow_repository.get(mock_workflow_id)

    mock_session.query.assert_called_once_with(Workflow)
    mock_query.get.assert_called_once_with(mock_workflow_id)
    assert workflow == mock_workflow


def test_workflow_repository_update(workflow_repository: WorkflowRepository, mock_session):
    mock_workflow = Mock(spec=Workflow)
    workflow_update_data = {"name": "New workflow name", "goal": "New goals"}

    result = workflow_repository.update(mock_workflow, workflow_update_data)

    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(mock_workflow)

    assert mock_workflow.name == workflow_update_data["name"]
    assert mock_workflow.goal == workflow_update_data["goal"]
    assert result == mock_workflow


def test_workflow_repository_delete(workflow_repository: WorkflowRepository, mock_session):
    mock_workflow = Mock(spec=Workflow)

    workflow_repository.delete(mock_workflow)

    mock_session.delete.assert_called_once_with(mock_workflow)
    mock_session.commit.assert_called_once()
