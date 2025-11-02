# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing

from google.protobuf.message import Message  # type: ignore

from pydantic import BaseModel, ConfigDict, Field

from .common_p2p import RequestMeta, VersionHeader
from .enums_p2p import AppRole, GameSystem


class GetServerSettingsRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    server_id: str = Field(default="")


class RoleMapping(BaseModel):
    map: "typing.Dict[str, AppRole]" = Field(default_factory=dict)


class ServerSettings(BaseModel):
    model_config = ConfigDict(validate_default=True)
    server_id: str = Field(default="")
    default_announcement_channel_id: str = Field(default="")
    default_system: GameSystem = Field(default=0)
    dm_notifications_enabled: bool = Field(default=False)
    role_mapping: RoleMapping = Field(default_factory=RoleMapping)
    mentionable_roles: typing.List[str] = Field(default_factory=list)


class UpdateServerSettingsRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    server_id: str = Field(default="")
    update: ServerSettings = Field(default_factory=ServerSettings)


class ServerSettingsResponse(BaseModel):
    settings: ServerSettings = Field(default_factory=ServerSettings)
    version: VersionHeader = Field(default_factory=VersionHeader)


class GetRoleMappingRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    server_id: str = Field(default="")


class UpdateRoleMappingRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    server_id: str = Field(default="")
    mapping: RoleMapping = Field(default_factory=RoleMapping)


class RoleMappingResponse(BaseModel):
    server_id: str = Field(default="")
    mapping: RoleMapping = Field(default_factory=RoleMapping)
    version: VersionHeader = Field(default_factory=VersionHeader)
