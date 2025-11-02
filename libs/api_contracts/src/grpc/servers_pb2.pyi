import common_pb2 as _common_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServerSettingsRequest(_message.Message):
    __slots__ = ("meta", "server_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    server_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., server_id: _Optional[str] = ...) -> None: ...

class UpdateServerSettingsRequest(_message.Message):
    __slots__ = ("meta", "server_id", "update")
    META_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    server_id: str
    update: ServerSettings
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., server_id: _Optional[str] = ..., update: _Optional[_Union[ServerSettings, _Mapping]] = ...) -> None: ...

class ServerSettings(_message.Message):
    __slots__ = ("server_id", "default_announcement_channel_id", "default_system", "dm_notifications_enabled", "role_mapping", "mentionable_roles")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ANNOUNCEMENT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    DM_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ROLE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    MENTIONABLE_ROLES_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    default_announcement_channel_id: str
    default_system: _enums_pb2.GameSystem
    dm_notifications_enabled: bool
    role_mapping: RoleMapping
    mentionable_roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_id: _Optional[str] = ..., default_announcement_channel_id: _Optional[str] = ..., default_system: _Optional[_Union[_enums_pb2.GameSystem, str]] = ..., dm_notifications_enabled: bool = ..., role_mapping: _Optional[_Union[RoleMapping, _Mapping]] = ..., mentionable_roles: _Optional[_Iterable[str]] = ...) -> None: ...

class ServerSettingsResponse(_message.Message):
    __slots__ = ("settings", "version")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    settings: ServerSettings
    version: _common_pb2.VersionHeader
    def __init__(self, settings: _Optional[_Union[ServerSettings, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class GetRoleMappingRequest(_message.Message):
    __slots__ = ("meta", "server_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    server_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., server_id: _Optional[str] = ...) -> None: ...

class UpdateRoleMappingRequest(_message.Message):
    __slots__ = ("meta", "server_id", "mapping")
    META_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    server_id: str
    mapping: RoleMapping
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., server_id: _Optional[str] = ..., mapping: _Optional[_Union[RoleMapping, _Mapping]] = ...) -> None: ...

class RoleMappingResponse(_message.Message):
    __slots__ = ("server_id", "mapping", "version")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    mapping: RoleMapping
    version: _common_pb2.VersionHeader
    def __init__(self, server_id: _Optional[str] = ..., mapping: _Optional[_Union[RoleMapping, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class RoleMapping(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _enums_pb2.AppRole
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_enums_pb2.AppRole, str]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[str, _enums_pb2.AppRole]
    def __init__(self, map: _Optional[_Mapping[str, _enums_pb2.AppRole]] = ...) -> None: ...
