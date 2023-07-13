import pytest

from unittest.mock import patch
from fastapi import HTTPException

from src.types.enums import Methodology, SecurityLevel
from src.models.v1.projects.project import Project
from src.schemas.v1.project_schema import ProjectCreateSchema, ProjectDeleteSchema, ProjectUpdateSchema
from src.api.v1.project_routes import project_create, project_delete, project_list, project_update


def test_project_create(mocker):
    """
    Test the project_create function to ensure it behaves as expected.

    This test uses a mock session and a mock UUID to create a deterministic testing environment.
    The project_create function is then called, and the returned project is compared to a mock project 
    with the same properties.

    Assertions are made to ensure that the properties of the returned project match the mock project,
    and that the correct methods on the mock session were called with the correct arguments.

    Args:
        mocker (MockerFixture): Pytest fixture that provides convenient APIs for mocking.

    Returns:
        None
    """
    mock_session = mocker.Mock()
    mock_uuid = "0286b74f-764a-4171-8d0e-1dd3815c985"

    with patch('uuid.uuid4', return_value=mock_uuid):
        expected_project = Project(
            id=mock_uuid,
            name="test",
            name_key="test",
            description="test description",
            methodology=Methodology.SCRUM,
            security_level=SecurityLevel.LEVEL_1
        )

        mock_project = ProjectCreateSchema(
            name="test",
            name_key="test",
            description="test description",
            methodology=Methodology.SCRUM,
            security_level=SecurityLevel.LEVEL_1
        )

        result = project_create(project=mock_project, session=mock_session)

    assert result.id == expected_project.id
    assert result.name == expected_project.name
    assert result.name_key == expected_project.name_key
    assert result.description == expected_project.description
    assert result.methodology == expected_project.methodology
    assert result.security_level == expected_project.security_level

    mock_session.add.assert_called_once_with(expected_project)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(expected_project)


def test_project_list(mocker):
    """Test the project_list function.

    The function should return a list of all projects in the database. In this unit test,
    we mock the session object and its query method, so that it returns a predefined list of projects.
    We then call the project_list function and verify that it returns the correct list of projects.

    Args:
        mocker: Pytest fixture that allows to conveniently use the powerful unittest.mock package.
    """
    # Arrange: Create a mock session object
    mock_session = mocker.Mock()

    # Arrange: Create a mock list of projects
    mock_projects = [
        Project(
            id="0286b74f-764a-4171-8d0e-1dd3815c985f",
            name="test",
            name_key="test",
            description="test description",
            methodology=Methodology.SCRUM,
            security_level=SecurityLevel.LEVEL_1
        ),
        Project(
            id="c83b2bef-d7d1-40db-89ab-12fd5c660a4e",
            name="test2",
            name_key="test2",
            description="test description 2",
            methodology=Methodology.KANBAN,
            security_level=SecurityLevel.LEVEL_2
        )
    ]

    # Arrange: Set up the mock session's query method to return the mock list of projects
    mock_session.query().all.return_value = mock_projects

    # Act: Call the project_list function
    result = project_list(session=mock_session)

    # Assert: Check that the function returned the correct list of projects
    assert result == mock_projects


def test_project_update(mocker):
    """
    This test ensures that the `project_update` function properly updates a project with the
    correct data when a valid project id and update data are provided. 
    It also checks if the function raises an HTTPException when the project id does not exist.
    """

    mock_session = mocker.Mock()

    # Mock existing project
    mock_project = Project(
        id="0286b74f-764a-4171-8d0e-1dd3815c985",
        name="test",
        name_key="test",
        description="test description",
        methodology=Methodology.SCRUM,
        security_level=SecurityLevel.LEVEL_1
    )

    # Mock updated project data
    updated_project_data = ProjectUpdateSchema(
        description="updated_test description",
        security_level=SecurityLevel.LEVEL_2
    )

    mock_session.query.return_value.get.return_value = mock_project

    result = project_update(
        project_id=mock_project.id,  # type: ignore
        project_update_schema=updated_project_data,
        session=mock_session
    )

    # Check if the correct project was updated with the correct data
    assert result.description == updated_project_data.description
    assert result.security_level == updated_project_data.security_level

    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(mock_project)

    # Mock a nonexistent project
    mock_session.query.return_value.get.return_value = None

    with pytest.raises(HTTPException) as e:
        project_update(
            project_id="nonexistent_project_id",
            project_update_schema=updated_project_data,
            session=mock_session
        )

    # Check if the exception has the correct status code and detail
    assert e.value.status_code == 404
    assert e.value.detail == "Project not found"


def test_project_delete(mocker):
    """
    This test ensures that the `project_delete` function deletes the specified project when given
    a valid project_id and name_key. It also verifies that the function correctly raises exceptions
    when provided with an invalid project_id or incorrect name_key.
    """

    mock_session = mocker.Mock()

    # Mock existing project
    mock_project = Project(
        id="0286b74f-764a-4171-8d0e-1dd3815c985f",
        name="test",
        name_key="test",
        description="test description",
        methodology=Methodology.SCRUM,
        security_level=SecurityLevel.LEVEL_1
    )

    # Mock delete data
    delete_project_data = ProjectDeleteSchema(
        name_key="test",
    )

    mock_session.query.return_value.get.return_value = mock_project

    result = project_delete(
        project_id=mock_project.id,  # type: ignore
        project_delete_schema=delete_project_data,
        session=mock_session
    )

    # Check if the correct project was deleted
    assert result == mock_project

    mock_session.delete.assert_called_once_with(mock_project)
    mock_session.commit.assert_called_once()

    # Mock a nonexistent project
    mock_session.query.return_value.get.return_value = None

    with pytest.raises(HTTPException) as e:
        project_delete(
            project_id="nonexistent_project_id",
            project_delete_schema=delete_project_data,
            session=mock_session
        )

    # Check if the exception has the correct status code and detail
    assert e.value.status_code == 404
    assert e.value.detail == "Project not found"

    # Mock incorrect name key
    mock_session.query.return_value.get.return_value = mock_project
    delete_project_data = ProjectDeleteSchema(
        name_key="incorrect_key",
    )

    with pytest.raises(HTTPException) as e:
        project_delete(
            project_id=mock_project.id,  # type: ignore
            project_delete_schema=delete_project_data,
            session=mock_session
        )

    # Check if the exception has the correct status code and detail
    assert e.value.status_code == 400
    assert e.value.detail == "Incorrect name key"
