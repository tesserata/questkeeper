from uuid import UUID

from qk_api_contracts.enums import GameSystem, SignupRole
from qk_api_contracts.grpc.sessions.models_pb2 import SessionInfo

from app.domain.common import VersionHeader
from app.domain.session import Session
from app.infrastructure.db.uow import UnitOfWork

# Session commands
async def create_session(
    payload: SessionInfo,
) -> tuple[Session, VersionHeader]:
    session = Session(
        server_id=payload.server_id,
        event_id=UUID(payload.event_id) if payload.event_id else None,
        title=payload.title,
        summary=payload.summary,
        system=GameSystem(payload.system),
        gm_user_id=payload.gm_user_id,
        vtt_link=payload.vtt_link,
        location=payload.location,
        additional_links=payload.additional_links,
        time=payload.time.ToDatetime(),
        duration_minutes=payload.duration_minutes,
        capacity=payload.capacity,
        role_mentions=payload.role_mentions,
    )

    async with UnitOfWork() as uow:
        await uow.sessions.create_session(session)
        version_header = session.version_header
        # await uow.outbox.enqueue(
        #     topic="discord.session.created",
        #     key=session_id,
        #     payload={"session_id": session_id, "version": version},
        # )
    return session, version_header

# Session queries
async def get_session(session_id: UUID) -> tuple[Session, VersionHeader]:
    pass

# Signup commands
async def signup(uow, *, session_id, user_id, role: SignupRole, character_id=None):
    agg = await uow.sessions.load(session_id, for_update=True)
    agg.signup(user_id=user_id, role=role, character_id=character_id)
    await uow.sessions.save(agg)
    v = agg.version
    await uow.outbox.enqueue(
        topic="discord.session.updated",
        key=session_id,
        payload={"session_id": session_id, "version": v},
    )
    return agg


async def switch_main_to_reserve(uow, *, session_id, user_id):
    agg = await uow.sessions.load(session_id, for_update=True)
    agg.switch_main_to_reserve(user_id=user_id)
    await uow.sessions.save(agg)
    v = agg.version
    await uow.outbox.enqueue(
        topic="discord.session.updated",
        key=session_id,
        payload={"session_id": session_id, "version": v},
    )
    return agg


async def claim_main_from_reserve(uow, *, session_id, user_id):
    agg = await uow.sessions.load(session_id, for_update=True)
    agg.claim_main_from_reserve(user_id=user_id)
    await uow.sessions.save(agg)
    v = agg.version
    await uow.outbox.enqueue(
        topic="discord.session.updated",
        key=session_id,
        payload={"session_id": session_id, "version": v},
    )
    return agg


async def leave(uow, *, session_id, user_id):
    agg = await uow.sessions.load(session_id, for_update=True)
    agg.leave(user_id=user_id)
    await uow.sessions.save(agg)
    v = agg.version
    await uow.outbox.enqueue(
        topic="discord.session.updated",
        key=session_id,
        payload={"session_id": session_id, "version": v},
    )
    return agg


async def attach_character(uow, *, session_id, user_id, character_id):
    agg = await uow.sessions.load(session_id, for_update=True)
    agg.attach_character(user_id=user_id, character_id=character_id)
    await uow.sessions.save(agg)
    v = agg.version
    await uow.outbox.enqueue(
        topic="discord.session.updated",
        key=session_id,
        payload={"session_id": session_id, "version": v},
    )
    return agg


async def set_capacity(uow, *, session_id, new_capacity: int):
    agg = await uow.sessions.load(session_id, for_update=True)
    agg.set_capacity(new_capacity=new_capacity)
    await uow.sessions.save(agg)
    v = agg.version
    await uow.outbox.enqueue(
        topic="discord.session.updated",
        key=session_id,
        payload={"session_id": session_id, "version": v},
    )
    return agg
