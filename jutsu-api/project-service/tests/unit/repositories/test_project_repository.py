import pytest

from unittest.mock import Mock

from src.core.exceptions.projects.project_exceptions import ProjectNotFoundException
from src.models.v1.projects.project import Project
from src.repositories.projects.project_repository import ProjectRepository


@pytest.fixture
def mock_session():
    return Mock()


@pytest.fixture
def project_repository(mock_session):
    return ProjectRepository(mock_session)


def test_project_repository_create(project_repository, mock_session):
    mock_project = Mock()

    project_repository.create(mock_project)

    mock_session.add.assert_called_once_with(mock_project)
    mock_session.commit_assert_called_once()
    mock_session.refresh.assert_called_once_with(mock_project)


def test_project_repository_get_all(project_repository, mock_session):
    mock_projects = [Mock(), Mock(), Mock()]
    mock_session.query.return_value.all.return_value = mock_projects

    actual_projects = project_repository.get_all()

    mock_session.query.assert_called_once_with(Project)
    mock_session.query.return_value.all.assert_called_once()
    assert actual_projects == mock_projects


def test_project_repository_get_project_or_404_found(project_repository, mock_session):
    mock_project = Mock()
    mock_session.query.return_value.get.return_value = mock_project

    project = project_repository.get_project_or_404('mock-id')

    mock_session.query.assert_called_once_with(Project)
    mock_session.query.return_value.get.assert_called_once_with('mock-id')
    assert project == mock_project


def test_project_repository_get_project_or_404_not_found(project_repository, mock_session):
    mock_session.query.return_value.get.return_value = None

    with pytest.raises(ProjectNotFoundException):
        project_repository.get_project_or_404('mock-id')

    mock_session.query.assert_called_once_with(Project)
    mock_session.query.return_value.get.assert_called_once_with('mock-id')


def test_project_repository_update(project_repository, mock_session):
    mock_project = Mock()
    mock_project.description = {"description": "Old description"}

    update_data = {"description": "New description"}

    project_repository.update(mock_project, update_data)

    assert mock_project.description == "New description"
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(mock_project)


def test_project_repository_delete(project_repository, mock_session):
    mock_project = Mock()

    project_repository.delete(mock_project)

    mock_session.delete.assert_called_once_with(mock_project)
    mock_session.commit.assert_called_once()
