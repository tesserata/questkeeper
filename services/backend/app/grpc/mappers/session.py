from uuid import UUID

from qk_api_contracts.enums import GameSystem, ScheduleStatus, SignupRole
from qk_api_contracts.grpc.sessions.models_pb2 import (
    Session,
    SessionInfo,
    SessionView,
    Signup,
    SignupInfo,
    SignupView,
)
from qk_api_contracts.grpc.sessions.models_pb2 import Session as PbSession
from qk_api_contracts.grpc.sessions.models_pb2 import SessionInfo as PbSessionInfo
from qk_api_contracts.grpc.sessions.models_pb2 import SessionSummary as PbSessionSummary
from qk_api_contracts.grpc.sessions.models_pb2 import SessionView as PbSessionView

from app.domain.character import Character
from app.domain.common import VersionHeader as DomainVersionHeader
from app.domain.session import Session as DomainSession
from app.domain.session import Signup as DomainSignup
from app.grpc.mappers._common import (
    _dt_to_ts,
    _enum_or_none,
    _ts_to_dt,
    _uuid_or_none,
    _version_from_pb,
    _version_to_pb,
)
from app.grpc.mappers.character import character_domain_to_pb


# Core helpers
def _session_to_info_pb(domain: DomainSession) -> PbSessionInfo:
    return PbSessionInfo(
        server_id=domain.server_id,
        event_id=str(domain.event_id) if domain.event_id else "",
        title=domain.title,
        description=domain.description,
        system=domain.system,
        gm_user_id=domain.gm_user_id,
        vtt_link=domain.vtt_link or "",
        location=domain.location or "",
        additional_links=list(domain.additional_links),
        time=_dt_to_ts(domain.time),
        duration_minutes=domain.duration_minutes,
        capacity=domain.capacity,
        role_mentions=list(domain.role_mentions),
    )


def _session_from_info_pb(
    info: SessionInfo,
    *,
    session_id: UUID | None = None,
    status: ScheduleStatus | None = None,
    channel_id: int | None = None,
    message_id: int | None = None,
    main_signups: list[DomainSignup] | None = None,
    reserve_signups: list[DomainSignup] | None = None,
    version_header: DomainVersionHeader | None = None,
) -> DomainSession:
    return DomainSession(
        session_id=session_id,
        server_id=info.server_id,
        event_id=_uuid_or_none(info.event_id),
        title=info.title,
        description=info.description,
        system=_enum_or_none(GameSystem, info.system),
        gm_user_id=info.gm_user_id,
        vtt_link=info.vtt_link,
        location=info.location,
        additional_links=list(info.additional_links),
        time=_ts_to_dt(info.time),
        duration_minutes=info.duration_minutes,
        capacity=info.capacity,
        role_mentions=list(info.role_mentions),
        status=_enum_or_none(ScheduleStatus, status),
        channel_id=channel_id,
        message_id=message_id,
        version_header=version_header or DomainVersionHeader(),
        main_signups=main_signups or [],
        reserve_signups=reserve_signups or [],
    )


def _signup_to_info_pb(domain: DomainSignup) -> SignupInfo:
    return SignupInfo(
        session_id=str(domain.session_id),
        user_id=domain.user_id,
        character_id=str(domain.character_id) if domain.character_id else "",
        role=domain.role,
    )


def _signup_from_info_pb(
    info: SignupInfo,
    *,
    version_header: DomainVersionHeader | None = None,
) -> DomainSignup:
    return DomainSignup(
        session_id=UUID(info.session_id),
        user_id=info.user_id,
        character_id=_uuid_or_none(info.character_id),
        role=_enum_or_none(SignupRole, info.role),
        version_header=version_header or DomainVersionHeader(),
    )


# --- Signup ---
# signup info
def signup_info_pb_to_domain(pb_obj: SignupInfo) -> DomainSignup:
    return _signup_from_info_pb(pb_obj)


def signup_domain_to_info_pb(domain: DomainSignup) -> SignupInfo:
    return _signup_to_info_pb(domain)


# signup
def signup_pb_to_domain(pb_obj: Signup) -> DomainSignup:
    return _signup_from_info_pb(
        pb_obj.info,
        version_header=_version_from_pb(pb_obj.version),
    )


def signup_domain_to_pb(domain: DomainSignup) -> Signup:
    return Signup(
        info=_signup_to_info_pb(domain),
        version=_version_to_pb(domain.version_header),
    )


# signup view
def signup_view_pb_to_domain(pb_obj: SignupView) -> DomainSignup:
    # view uses a nested character summary; just pull the id
    return DomainSignup(
        session_id=UUID(pb_obj.session_id),
        user_id=pb_obj.user_id,
        character_id=_uuid_or_none(pb_obj.character.character_id),
        role=_enum_or_none(SignupRole, pb_obj.role),
    )


def signup_domain_to_view_pb(
    signup: DomainSignup,
    character: Character,
) -> SignupView:
    return SignupView(
        user_id=signup.user_id,
        session_id=str(signup.session_id),
        role=signup.role,
        character=character_domain_to_pb(character),
    )


# --- Session ---
# session info
def session_info_pb_to_domain(pb_obj: SessionInfo) -> DomainSession:
    return _session_from_info_pb(pb_obj)


def session_domain_to_info_pb(domain: DomainSession) -> PbSessionInfo:
    return _session_to_info_pb(domain)


# session
def session_pb_to_domain(pb_obj: Session) -> DomainSession:
    return _session_from_info_pb(
        pb_obj.info,
        session_id=UUID(pb_obj.session_id),
        status=_enum_or_none(ScheduleStatus, pb_obj.status),
        channel_id=pb_obj.channel_id or None,
        message_id=pb_obj.message_id or None,
        version_header=_version_from_pb(pb_obj.version),
    )


def session_domain_to_pb(domain: DomainSession) -> PbSession:
    pb = PbSession(
        session_id=str(domain.session_id),
        info=_session_to_info_pb(domain),
        status=domain.status,
        channel_id=domain.channel_id,
        message_id=domain.message_id,
        version=_version_to_pb(domain.version_header),
    )

    return pb


# session view
def session_view_pb_to_domain(pb_obj: SessionView) -> DomainSession:
    main_signups = [signup_view_pb_to_domain(s) for s in pb_obj.main_signups]
    reserve_signups = [signup_view_pb_to_domain(s) for s in pb_obj.reserve_signups]

    return _session_from_info_pb(
        pb_obj.info,
        session_id=UUID(pb_obj.session_id),
        status=_enum_or_none(ScheduleStatus, pb_obj.status),
        channel_id=pb_obj.channel_id or None,
        message_id=pb_obj.message_id or None,
        main_signups=main_signups,
        reserve_signups=reserve_signups,
    )


def session_domain_to_view_pb(
    session: DomainSession,
    *,
    characters: dict[UUID, Character],
) -> PbSessionView:
    main_views: list[SignupView] = []
    for signup in session.main_signups:
        view = signup_domain_to_view_pb(signup, characters[signup.character_id])
        main_views.append(view)

    reserve_views: list[SignupView] = []
    for signup in session.reserve_signups:
        view = signup_domain_to_view_pb(signup, characters[signup.character_id])
        main_views.append(view)

    return PbSessionView(
        session_id=str(session.session_id),
        info=_session_to_info_pb(session),
        channel_id=session.channel_id or 0,
        message_id=session.message_id or 0,
        status=session.status,
        seats_taken=len(session.main_signups),
        main_signups=main_views,
        reserve_signups=reserve_views,
    )


# session summary
# def session_summary_pb_to_domain(pb_obj: SessionSummary) -> DomainSession:
#     return DomainSession(
#         pb_obj.info,
#         session_id=UUID(pb_obj.session_id),
#         status=_enum_or_none(ScheduleStatus, pb_obj.status),
#         channel_id=pb_obj.channel_id or None,
#         message_id=pb_obj.message_id or None,
#         main_signups=main_signups,
#         reserve_signups=reserve_signups,
#     )


def session_domain_to_summary_pb(
    session: DomainSession,
) -> PbSessionSummary:
    return PbSessionSummary(
        title=session.title,
        game_system=session.system,
        gm_user_id=session.gm_user_id,
        status=session.status,
        time=_dt_to_ts(session.time),
        capacity=session.capacity,
        seats_taken=session.seats_taken,
        server_id=session.server_id,
        channel_id=session.channel_id or 0,
        message_id=session.message_id or 0,
        session_id=str(session.session_id),
    )
