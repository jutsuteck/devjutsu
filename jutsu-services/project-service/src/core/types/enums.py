from enum import Enum


class Methodology(Enum):
    SCRUM = "Scrum"
    KANBAN = "Kanban"


class SecurityLevel(Enum):
    LEVEL_1 = "Level 1"
    LEVEL_2 = "Level 2"
    LEVEL_3 = "Level 3"


class WorkItemType(Enum):
    BUG = "Bug"
    USER_STORY = "User Story"
    WORK_ITEM = "Work Item"
