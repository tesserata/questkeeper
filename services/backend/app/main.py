from fastapi import FastAPI

from app.api.exception_handlers import register_exception_handlers
from app.api.routers.v1 import characters
from app.config import get_config

settings = get_config()

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    root_path=settings.API_PREFIX,
)

register_exception_handlers(app)
app.include_router(characters.router)


@app.get("/info")
async def info():
    return {
        "project_name": settings.PROJECT_NAME,
        "debug_mode": settings.DEBUG,
    }

