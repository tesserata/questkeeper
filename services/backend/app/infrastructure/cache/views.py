from redis.asyncio import Redis


def view_pointer_key(session_id: str) -> str:
    return f"session_view:{session_id}:current"


def view_blob_key(session_id: str, version: int) -> str:
    return f"session_view:{session_id}:v{version}"


async def publish_view_cache(redis: Redis, session_id: str, version: int, view_json: str) -> None:
    await redis.set(view_blob_key(session_id, version), view_json, ex=86400)
    await redis.set(view_pointer_key(session_id), str(version), ex=86400)
