from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.models.v1.users import Role, Permission

DEFAULT_ROLES = [
    "Individual User",
    "Team Member",
    "Team Lead",
    "Organization Member",
    "Organization Admin"
]

DEFAULT_PERMISSIONS = [
    "create_personal_project",
    "manage_personal_project",
    "view_team_project",
    "edit_team_project",
    "create_team",
    "manage_team",
    "manage_all_team_projects",
    "view_org_projects",
    "edit_assigned_org_project",
    "create_organization",
    "manage_organization",
    "manage_all_organization"
]


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
    for role_name in DEFAULT_ROLES:
        result = await (
            session.execute(select(Role).filter_by(name=role_name))
        )
        role = result.scalars().first()

        if not role:
            session.add(Role(name=role_name))

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
    for perm_name in DEFAULT_PERMISSIONS:
        result = await (
            session.execute(select(Permission).filter_by(name=perm_name))
        )
        perm = result.scalars().first()

        if not perm:
            session.add(Permission(name=perm_name))

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
    result = await session.execute(
        select(Role).options(joinedload(Role.permissions)
                             ).filter_by(name=role_name)
    )
    role = result.scalars().first()

    if role:
        for perm_name in permissions:
            result = await (
                session.execute(select(Permission).filter_by(name=perm_name))
            )
            perm = result.scalars().first()
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
