# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
from enum import IntEnum

from pydantic import BaseModel


class SignupRole(IntEnum):
    SIGNUP_ROLE_UNSPECIFIED = 0
    SIGNUP_ROLE_MAIN = 1
    SIGNUP_ROLE_RESERVE = 2


class AppRole(IntEnum):
    ROLE_ADMIN = 0
    ROLE_GM = 1
    ROLE_PLAYER = 2


class GameSystem(IntEnum):
    PATHFINDER_1E = 0
    PATHFINDER_2E = 1
    DND_5E = 2
    DSA_5 = 3


class Seat(IntEnum):
    SEAT_MAIN = 0
    SEAT_RESERVE = 1


class SessionStatus(IntEnum):
    SESSION_UNSPECIFIED = 0
    SESSION_DRAFT = 1
    SESSION_PUBLISHED = 2
    SESSION_CANCELLED = 3
    SESSION_COMPLETED = 4


class EventStatus(IntEnum):
    EVENT_UNSPECIFIED = 0
    EVENT_DRAFT = 1
    EVENT_PUBLISHED = 2
    EVENT_CANCELLED = 3
    EVENT_COMPLETED = 4
