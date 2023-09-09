from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.core.enums import PermissionsEnum, RolesEnum
from src.models.v1.users import Role, Permission
from src.repositories.permission_repository import PermissionRepository
from src.repositories.role_repository import RoleRepository


async def seed_roles(session: AsyncSession):
    """
    Seed the database with default roles.

    This function iterates over the DEFAULT_ROLES list and adds any role
    that doesn't already exist in the database.

    Args:
        session (AsyncSession): The database session to use for operations.

    Returns:
        None
    """
    role_repo = RoleRepository(session)

    for role in RolesEnum:
        existing_role = await role_repo.get_by_name(role.value)

        if not existing_role:
            session.add(Role(name=role.value))

        await session.commit()


async def seed_permissions(session: AsyncSession):
    """
    Seed the database with default permissions.

    This function iterates over the DEFAULT_PERMISSIONS list and adds any permission
    that doesn't already exist in the database.

    Args:
        session (AsyncSession): The database session to use for operations.

    Returns:
        None
    """
    permission_repo = PermissionRepository(session)

    for perm in PermissionsEnum:
        existing_perm = await permission_repo.get_by_name(perm.value)

        if not existing_perm:
            session.add(Permission(name=perm.value))

    await session.commit()


async def assign_permissions_to_role(
        session: AsyncSession,
        role_name: str,
        permissions: list):
    """
    Assign a list of permissions to a specific role.

    This function fetches the specified role from the database and assigns
    the provided list of permissions to it.

    Args:
        session (AsyncSession): The database session to use for operations.
        role_name (str): The name of the role to which permissions should be assigned.
        permissions (list): A list of permission names to assign to the role.

    Returns:
        None
    """
    role_repo = RoleRepository(session)
    permission_repo = PermissionRepository(session)

    role = await role_repo.get_by_name_with_permissions(role_name)

    if role:
        for perm_name in permissions:
            perm = await permission_repo.get_by_name(perm_name)
            if perm:
                role.permissions.append(perm)


async def setup_role_permissions(session: AsyncSession):
    """
    Set up default permissions for all roles.

    This function assigns the default set of permissions to each role in the
    system based on predefined lists.

    Args:
        session (AsyncSession): The database session to use for operations.

    Returns:
        None
    """
    await assign_permissions_to_role(session, "Individual User", ["create_personal_project", "manage_personal_project"])  # noqa: E501
    await assign_permissions_to_role(session, "Team Member", ["view_team_project", "edit_team_project"])  # noqa: E501
    await assign_permissions_to_role(session, "Team Lead", ["create_team", "manage_team", "manage_all_team_projects"])  # noqa: E501
    await assign_permissions_to_role(session, "Organization Member", ["view_org_projects", "edit_assigned_org_project"])  # noqa: E501
    await assign_permissions_to_role(session, "Organization Admin", ["create_organization", "manage_organization", "manage_all_organization"])  # noqa: E501
