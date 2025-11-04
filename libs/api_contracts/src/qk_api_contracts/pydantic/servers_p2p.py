# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing

from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel, Field


class GetServerSettingsRequest(BaseModel):
    server_id: str = Field(default="")


class ServerSettings(BaseModel):
    server_id: str = Field(default="")
    default_announcement_channel_id: str = Field(default="")
    default_system: str = Field(default="")
    dm_notifications_enabled: bool = Field(default=False)
    role_mapping: "typing.Dict[str, str]" = Field(default_factory=dict)
    mentionable_roles: typing.List[str] = Field(default_factory=list)


class GetRoleMappingRequest(BaseModel):
    server_id: str = Field(default="")


class RoleMapping(BaseModel):
    server_id: str = Field(default="")
    mapping: "typing.Dict[str, str]" = Field(default_factory=dict)
