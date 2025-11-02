# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing
from datetime import datetime

from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .common_p2p import Page, PageRequest, RequestMeta, VersionHeader
from .enums_p2p import Seat


class Signup(BaseModel):
    model_config = ConfigDict(validate_default=True)
    session_id: str = Field(default="")
    user_id: int = Field(default=0)
    character_id: str = Field(default="")
    seat: Seat = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class CreateSignupRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    signup: Signup = Field(default_factory=Signup)


class GetSignupRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")
    signup_id: str = Field(default="")


class DeleteSignupRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")
    signup_id: str = Field(default="")


class UpdateCharacter(BaseModel):
    character_id: str = Field(default="")


class UpdateSeat(BaseModel):
    model_config = ConfigDict(validate_default=True)
    seat: Seat = Field(default=0)


class UpdateSignupRequest(BaseModel):
    _one_of_dict = {"UpdateSignupRequest.patch": {"fields": {"character", "seat"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")
    signup_id: str = Field(default="")
    expected_version: int = Field(default=0)
    character: UpdateCharacter = Field(default_factory=UpdateCharacter)
    seat: UpdateSeat = Field(default_factory=UpdateSeat)


class ListSignupsRequest(BaseModel):
    model_config = ConfigDict(validate_default=True)
    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")
    seat: Seat = Field(default=0)
    page: PageRequest = Field(default_factory=PageRequest)


class ListSignupsResponse(BaseModel):
    items: typing.List[Signup] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)


class SignupResponse(BaseModel):
    signup: Signup = Field(default_factory=Signup)
    version: VersionHeader = Field(default_factory=VersionHeader)
