from fastapi import FastAPI

from app.api.routers.v1 import characters
from app.config import get_config


def create_app() -> FastAPI:
    settings = get_config()

    app_ = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        root_path=settings.API_PREFIX,
    )

    app_.include_router(characters.router)

    @app_.get("/info")
    async def info():
        return {
            "project_name": settings.PROJECT_NAME,
            "debug_mode": settings.DEBUG,
        }

    return app_


app = create_app()
