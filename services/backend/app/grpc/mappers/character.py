from uuid import UUID

from qk_api_contracts.enums import GameSystem
from qk_api_contracts.grpc.characters.models_pb2 import (
    Character as PbCharacter,
)
from qk_api_contracts.grpc.characters.models_pb2 import (
    CharacterInfo as PbCharacterInfo,
)
from qk_api_contracts.grpc.characters.models_pb2 import PlayRecord as PbPlayRecord

from app.domain.character import Character as DomainCharacter
from app.domain.character import PlayRecord as DomainPlayRecord
from app.domain.common import VersionHeader as DomainVersionHeader
from app.grpc.mappers._common import (
    _dt_to_ts,
    _enum_or_none,
    _ts_to_dt,
    _uuid_or_none,
    _version_from_pb,
    _version_to_pb,
)


# helper functions
def _character_from_info_pb(
    info: PbCharacterInfo,
    *,
    character_id: UUID | None = None,
    version_header: DomainVersionHeader | None = None,
) -> DomainCharacter:
    kwargs: dict = dict(
        user_id=info.user_id,
        system=_enum_or_none(GameSystem, info.system),
        name=info.name,
        class_name=info.class_name,
        subclass_name=info.subclass_name,
        level=info.level or 1,
        race=info.race,
        notes=info.notes,
        version_header=version_header or DomainVersionHeader(),
    )

    if character_id:
        kwargs["character_id"] = character_id

    return DomainCharacter(**kwargs)


def _character_to_info_pb(domain: DomainCharacter) -> PbCharacterInfo:
    return PbCharacterInfo(
        user_id=domain.user_id,
        system=domain.system,
        name=domain.name,
        class_name=domain.class_name,
        subclass_name=domain.subclass_name,
        level=domain.level,
        race=domain.race,
        notes=domain.notes,
    )


# protobuf to domain


def character_info_pb_to_domain(pb_obj: PbCharacterInfo) -> DomainCharacter:
    return _character_from_info_pb(pb_obj)


def character_pb_to_domain(pb_obj: PbCharacter) -> DomainCharacter:
    return _character_from_info_pb(
        pb_obj.info,
        character_id=_uuid_or_none(pb_obj.character_id),
        version_header=_version_from_pb(pb_obj.version),
    )


def play_record_pb_to_domain(pb_obj: PbPlayRecord) -> DomainPlayRecord:
    return DomainPlayRecord(
        session_title=pb_obj.session_title,
        gm_user_id=pb_obj.gm_user_id,
        time=_ts_to_dt(pb_obj.time),
        server_id=pb_obj.server_id,
        channel_id=pb_obj.channel_id,
        message_id=pb_obj.message_id,
    )


# domain to protobuf


def character_domain_to_info_pb(domain: DomainCharacter) -> PbCharacterInfo:
    return _character_to_info_pb(domain)


def character_domain_to_pb(domain: DomainCharacter) -> PbCharacter:
    pb = PbCharacter(
        character_id=str(domain.character_id),
        info=_character_to_info_pb(domain),
        version=_version_to_pb(domain.version_header),
    )
    return pb


def play_record_domain_to_pb(domain: DomainPlayRecord) -> PbPlayRecord:
    pb = PbPlayRecord(
        session_title=domain.session_title,
        gm_user_id=domain.gm_user_id,
        time=_dt_to_ts(domain.time),
        server_id=domain.server_id,
        channel_id=domain.channel_id,
        message_id=domain.message_id,
    )
    return pb
