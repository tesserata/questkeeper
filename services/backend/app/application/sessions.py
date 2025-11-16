from uuid import UUID

from qk_api_contracts.enums import SignupRole

from app.domain.common import VersionHeader
from app.domain.session import Session
from app.infrastructure.db.uow import UnitOfWork


# Session commands
async def create_session(
    payload: Session,
) -> Session:
    async with UnitOfWork() as uow:
        await uow.sessions.create_session(payload)
        # await uow.outbox.enqueue(
        #     topic="discord.session.created",
        #     key=session_id,
        #     payload={"session_id": session_id, "version": version},
        # )
    return payload


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
