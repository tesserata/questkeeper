from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SignupRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNUP_ROLE_UNSPECIFIED: _ClassVar[SignupRole]
    SIGNUP_ROLE_MAIN: _ClassVar[SignupRole]
    SIGNUP_ROLE_RESERVE: _ClassVar[SignupRole]

class AppRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_ADMIN: _ClassVar[AppRole]
    ROLE_GM: _ClassVar[AppRole]
    ROLE_PLAYER: _ClassVar[AppRole]

class GameSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PATHFINDER_1E: _ClassVar[GameSystem]
    PATHFINDER_2E: _ClassVar[GameSystem]
    DND_5E: _ClassVar[GameSystem]
    DSA_5: _ClassVar[GameSystem]

class Seat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEAT_MAIN: _ClassVar[Seat]
    SEAT_RESERVE: _ClassVar[Seat]

class SessionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_UNSPECIFIED: _ClassVar[SessionStatus]
    SESSION_DRAFT: _ClassVar[SessionStatus]
    SESSION_PUBLISHED: _ClassVar[SessionStatus]
    SESSION_CANCELLED: _ClassVar[SessionStatus]
    SESSION_COMPLETED: _ClassVar[SessionStatus]

class EventStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_UNSPECIFIED: _ClassVar[EventStatus]
    EVENT_DRAFT: _ClassVar[EventStatus]
    EVENT_PUBLISHED: _ClassVar[EventStatus]
    EVENT_CANCELLED: _ClassVar[EventStatus]
    EVENT_COMPLETED: _ClassVar[EventStatus]
SIGNUP_ROLE_UNSPECIFIED: SignupRole
SIGNUP_ROLE_MAIN: SignupRole
SIGNUP_ROLE_RESERVE: SignupRole
ROLE_ADMIN: AppRole
ROLE_GM: AppRole
ROLE_PLAYER: AppRole
PATHFINDER_1E: GameSystem
PATHFINDER_2E: GameSystem
DND_5E: GameSystem
DSA_5: GameSystem
SEAT_MAIN: Seat
SEAT_RESERVE: Seat
SESSION_UNSPECIFIED: SessionStatus
SESSION_DRAFT: SessionStatus
SESSION_PUBLISHED: SessionStatus
SESSION_CANCELLED: SessionStatus
SESSION_COMPLETED: SessionStatus
EVENT_UNSPECIFIED: EventStatus
EVENT_DRAFT: EventStatus
EVENT_PUBLISHED: EventStatus
EVENT_CANCELLED: EventStatus
EVENT_COMPLETED: EventStatus
