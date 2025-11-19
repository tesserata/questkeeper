from datetime import UTC, datetime
from typing import TypeVar
from uuid import UUID

from google.protobuf.timestamp_pb2 import Timestamp
from qk_api_contracts.grpc.common_pb2 import VersionHeader as PbVersionHeader

from app.domain.common import VersionHeader as DomainVersionHeader

StrEnum = TypeVar("StrEnum")


def _version_from_pb(pb: PbVersionHeader | None) -> DomainVersionHeader:
    if not pb:
        return DomainVersionHeader()
    return DomainVersionHeader(
        version=pb.version,
        created_at=_ts_to_dt(pb.created_at),
        updated_at=_ts_to_dt(pb.updated_at),
    )


def _version_to_pb(version: DomainVersionHeader | None) -> PbVersionHeader | None:
    if not version:
        return None

    pb = PbVersionHeader(
        version=version.version,
        created_at=_dt_to_ts(version.created_at),
        updated_at=_dt_to_ts(version.updated_at),
    )
    return pb


def _ts_to_dt(ts: Timestamp | None) -> datetime | None:
    if not ts or not (ts.seconds or ts.nanos):
        return None
    return ts.ToDatetime().replace(tzinfo=UTC)


def _dt_to_ts(dt: datetime | None) -> Timestamp | None:
    if not dt:
        return None
    ts = Timestamp()
    ts.FromDatetime(dt)
    return ts


def _uuid_or_none(value: str | None) -> UUID | None:
    return UUID(value) if value else None


def _enum_or_none[StrEnum](enum_cls: type[StrEnum], value: str | None) -> StrEnum:
    return enum_cls(value) if value else None
