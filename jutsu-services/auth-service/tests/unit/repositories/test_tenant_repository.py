import pytest

from unittest.mock import AsyncMock, MagicMock

from sqlalchemy import Select

from src.models.v1.users import Tenant
from src.repositories.tenant_repository import TenantRepository


@pytest.fixture
def mock_session():
    mock = MagicMock()
    mock.commit = AsyncMock()
    mock.execute = AsyncMock()
    return mock


@pytest.fixture
def tenant_repository(mock_session):
    return TenantRepository(mock_session)


@pytest.mark.asyncio
async def test_repository_add_tenant(mock_session, tenant_repository):
    # Arrange
    test_tenant = Tenant(
        id="50d726fb-e22c-4f56-b2cb-5e4ba22cde03",
        name="Chatterbot"
    )

    # Act
    result = await tenant_repository.add(test_tenant)

    # Assert
    mock_session.add.assert_called_once_with(test_tenant)
    mock_session.commit.called_once()
    assert result == test_tenant
