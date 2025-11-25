from enum import StrEnum


class AppRole(StrEnum):
    ADMIN = "Server administrator"
    GM = "Game master"
    PLAYER = "Player"


class GameSystem(StrEnum):
    PATHFINDER_1E = "Pathfinder 1E"
    PATHFINDER_2E = "Pathfinder 2E"
    DND_5E = "D&D 5E"
    DSA_5 = "DSA 5E"


class SignupRole(StrEnum):
    MAIN = "Main"
    RESERVE = "Reserve"


class ScheduleStatus(StrEnum):
    DRAFT = "Draft"
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
