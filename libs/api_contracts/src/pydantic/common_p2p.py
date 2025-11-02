# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing
from datetime import datetime

from google.protobuf.message import Message  # type: ignore

from pydantic import BaseModel, ConfigDict, Field

from .enums_p2p import AppRole


class RequestMeta(BaseModel):
    """
    Request wrappers
    """

    model_config = ConfigDict(validate_default=True)
    request_id: str = Field(default="")
    idempotency_key: str = Field(default="")
    tenant_server_id: str = Field(default="")
    user_id: str = Field(default="")
    app_roles: typing.List[AppRole] = Field(default_factory=list)
    if_none_match: str = Field(default="")


class PageRequest(BaseModel):
    page_size: int = Field(default=0)
    page_token: str = Field(default="")


class Page(BaseModel):
    next_page_token: str = Field(default="")
    total_size: int = Field(default=0)


class VersionHeader(BaseModel):
    """
    Versioned view header for cache keys & weak ETags like W/"session:{id}:v{n}"
    """

    version: int = Field(default=0)
    weak_etag: str = Field(default="")
    updated_at: datetime = Field(default_factory=datetime.now)
