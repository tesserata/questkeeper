from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetServerSettingsRequest(_message.Message):
    __slots__ = ("server_id",)
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    def __init__(self, server_id: _Optional[str] = ...) -> None: ...

class ServerSettings(_message.Message):
    __slots__ = ("server_id", "default_announcement_channel_id", "default_system", "dm_notifications_enabled", "role_mapping", "mentionable_roles")
    class RoleMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ANNOUNCEMENT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    DM_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ROLE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    MENTIONABLE_ROLES_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    default_announcement_channel_id: str
    default_system: str
    dm_notifications_enabled: bool
    role_mapping: _containers.ScalarMap[str, str]
    mentionable_roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_id: _Optional[str] = ..., default_announcement_channel_id: _Optional[str] = ..., default_system: _Optional[str] = ..., dm_notifications_enabled: bool = ..., role_mapping: _Optional[_Mapping[str, str]] = ..., mentionable_roles: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRoleMappingRequest(_message.Message):
    __slots__ = ("server_id",)
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    def __init__(self, server_id: _Optional[str] = ...) -> None: ...

class RoleMapping(_message.Message):
    __slots__ = ("server_id", "mapping")
    class MappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    mapping: _containers.ScalarMap[str, str]
    def __init__(self, server_id: _Optional[str] = ..., mapping: _Optional[_Mapping[str, str]] = ...) -> None: ...
