import pytest

from unittest.mock import Mock, patch
from src.core.exceptions.projects.project_exceptions import IncorrectProjectNameKeyException
from src.core.types.enums import Methodology, SecurityLevel
from src.models.v1.projects.project import Project

from src.services.projects.project_service import ProjectService


@pytest.fixture
def mock_session():
    return Mock()


@pytest.fixture
def project_service(mock_session) -> ProjectService:
    return ProjectService(mock_session)


def test_project_service_create(project_service, environment):
    mock_project_data = {
        "name": "chatterbot",
        "name_key": "CHA",
        "description": "An AI chat app",
        "methodology": Methodology.SCRUM,
        "security_level": SecurityLevel.LEVEL_1
    }
    mock_project = Mock()
    mock_workflow = Mock()

    with patch.object(project_service.project_repository, "create", return_value=mock_project) as mock_create:
        with patch.object(project_service, "create_default_project_workflow", return_value=mock_workflow) as mock_create_workflow:
            with patch.object(project_service, "create_default_workflow_states") as mock_create_workflow_states:

                actual_project = project_service.create_project(
                    mock_project_data)

                mock_create.assert_called_once()
                created_project = mock_create.call_args[0][0]
                assert isinstance(created_project, Project)
                assert created_project.name == mock_project_data["name"]
                assert created_project.description == mock_project_data["description"]

                mock_create_workflow.assert_called_once_with(created_project)

                mock_create_workflow_states.assert_called_once_with(
                    mock_workflow)

                assert isinstance(actual_project, Project)
                assert actual_project.name == mock_project_data["name"]
                assert actual_project.name_key == mock_project_data["name_key"]
                assert actual_project.description == mock_project_data["description"]
                assert actual_project.methodology == mock_project_data["methodology"]
                assert actual_project.security_level == mock_project_data["security_level"]


def test_project_service_get_all(project_service, environment):
    mock_projects = [Mock(), Mock()]

    with patch.object(project_service.project_repository, 'get_all', return_value=mock_projects) as mock_get_all:
        result = project_service.get_all_projects()

        mock_get_all.called_once()

        assert result == mock_projects
