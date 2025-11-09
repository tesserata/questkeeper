from uuid import UUID

from qk_api_contracts.enums import GameSystem, SignupRole
from qk_api_contracts.grpc.sessions.models_pb2 import SessionInfo

from app.domain.common import VersionHeader
from app.domain.session import Session
from app.infrastructure.db.uow import UnitOfWork
from app.infrastructure.projections.sessions_view import update_view


async def create_session(
    request: SessionInfo,
) -> tuple[Session, VersionHeader]:
    session = Session(
        server_id=request.server_id,
        event_id=UUID(request.event_id) if request.event_id else None,
        title=request.title,
        summary=request.summary,
        system=GameSystem(request.system),
        gm_user_id=request.gm_user_id,
        vtt_link=request.vtt_link,
        location=request.location,
        additional_links=list(request.additional_links),
        time=request.time.ToDatetime(),
        duration_minutes=request.duration_minutes,
        capacity=request.capacity,
        role_mentions=list(request.role_mentions),
    )

    async with UnitOfWork() as uow:
        await uow.sessions.create(session)
        version_header = session.version_header
        # await update_view(uow.session, session.session_id, version_header.version)
        # await uow.outbox.enqueue(
        #     topic="discord.session.created",
        #     key=session_id,
        #     payload={"session_id": session_id, "version": version},
        # )
        return session, version_header


async def signup(uow, *, session_id, user_id, role: SignupRole, character_id=None):
    agg = await uow.sessions.load(session_id, for_update=True)
    agg.signup(user_id=user_id, role=role, character_id=character_id)
    await uow.sessions.save(agg)
    v = agg.version
    await update_view(uow.session, session_id, v)
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
    await update_view(uow.session, session_id, v)
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
    await update_view(uow.session, session_id, v)
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
    await update_view(uow.session, session_id, v)
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
    await update_view(uow.session, session_id, v)
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
    await update_view(uow.session, session_id, v)
    await uow.outbox.enqueue(
        topic="discord.session.updated",
        key=session_id,
        payload={"session_id": session_id, "version": v},
    )
    return agg
