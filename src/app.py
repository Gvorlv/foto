"""Модуль для запуска FASTAPI."""

from fastapi import FastAPI

from files.routing import router as files_router
from posts.routing import router as posts_router
from settings import settings
from users.routing import router as users_router


def create_app() -> FastAPI:
    if not settings.PATH_FILES.is_dir():
        settings.PATH_FILES.mkdir()
    return FastAPI()


app = create_app()
app.include_router(users_router, prefix="/api/v1", tags=["api/v1"])
app.include_router(posts_router, prefix="/api/v1", tags=["api/v1"])
app.include_router(files_router, prefix="/api/v1", tags=["api/v1"])


@app.get("/")
def read_root() -> dict[str, str]:
    """Тестовый эндпоинт.

    Returns
    -------
        dict[str, str]: тестовый словарь.

    """
    return {"Hello": "World"}
