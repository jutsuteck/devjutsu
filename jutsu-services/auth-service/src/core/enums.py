from enum import Enum


class RolesEnum(str, Enum):
    INDIVIDUAL_USER = "Individual User"
    TEAM_MEMBER = "Team Member"
    TEAM_LEAD = "Team Lead"
    ORGANIZATION_MEMBER = "Organization Member"
    ORGANIZATION_ADMIN = "Organization Admin"


class PermissionsEnum(str, Enum):
    CREATE_PERSONAL_PROJECT = "create_personal_project"
    MANAGE_PERSONAL_PROJECT = "manage_personal_project"
    VIEW_TEAM_PROJECT = "view_team_project"
    EDIT_TEAM_PROJECT = "edit_team_project"
    CREATE_TEAM = "create_team"
    MANAGE_TEAM = "manage_team"
    MANAGE_ALL_TEAM_PROJECTS = "manage_all_team_projects"
    VIEW_ORG_PROJECTS = "view_org_projects"
    EDIT_ASSIGNED_ORG_PROJECT = "edit_assigned_org_project"
    CREATE_ORGANIZATION = "create_organization"
    MANAGE_ORGANIZATION = "manage_organization"
    MANAGE_ALL_ORGANIZATION = "manage_all_organization"
