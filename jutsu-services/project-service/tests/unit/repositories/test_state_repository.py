import pytest

from unittest.mock import Mock
from sqlmodel import Session
from src.core.exceptions.projects.state_exceptions import StateNotFoundException

from src.models.v1.projects.state import State
from src.repositories.projects.state_repository import StateRepository


@pytest.fixture
def mock_session():
    return Mock(spec=Session)


@pytest.fixture
def state_repository(mock_session):
    return StateRepository(mock_session)


def test_state_repository_add(state_repository: StateRepository, mock_session):
    mock_state = Mock()

    state_repository.add(mock_state)

    mock_session.add.assert_called_once_with(mock_state)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(mock_state)


def test_state_reposity_filter_by_workflow(state_repository: StateRepository, mock_session):
    # Prepare data
    mock_workflow_id = "mock_workflow_id"
    mock_states = [Mock(spec=State), Mock(spec=State)]

    # Mock session.query().filter_by().all()
    mock_query = mock_session.query.return_value
    mock_filtered_query = mock_query.filter_by.return_value
    mock_filtered_query.all.return_value = mock_states

    # Call the method
    states = state_repository.filter_by_workflow(mock_workflow_id)

    # Assert the results
    mock_session.query.assert_called_once_with(State)
    mock_query.filter_by.assert_called_once_with(workflow_id=mock_workflow_id)
    assert states == mock_states


def test_state_repository_get(state_repository: StateRepository, mock_session):
    # Prepare data
    mock_state_id = "mock_state_id"
    mock_state = Mock(spec=State)

    # Mock session.query().get()
    mock_query = mock_session.query.return_value
    mock_query.get.return_value = mock_state

    # Call the method
    state = state_repository.get(mock_state_id)

    # Assert the results
    mock_session.query.assert_called_once_with(State)
    mock_query.get.assert_called_once_with(mock_state_id)
    assert state == mock_state


def test_state_repository_update(state_repository: StateRepository, mock_session):
    # Prepare data
    mock_state = Mock(spec=State)
    state_update_data = {"name": "New name"}

    # Call the method
    result = state_repository.update(mock_state, state_update_data)

    # Assert that the session commit was called
    mock_session.commit.assert_called_once()
    # Assert that the session refresh was called with the correct argument
    mock_session.refresh.assert_called_once_with(mock_state)

    # Assert that the correct attributes were set
    assert mock_state.name == "New name"
    # Assert the method result
    assert result == mock_state


def test_state_repository_delete(state_repository: StateRepository, mock_session):
    mock_state = Mock(spec=State)

    state_repository.delete(mock_state)

    mock_session.delete.assert_called_once_with(mock_state)
    mock_session.commit.assert_called_once()
