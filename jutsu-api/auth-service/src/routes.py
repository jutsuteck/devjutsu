from fastapi import FastAPI

from src.core.auth.auth_backend import auth_backend
from src.core.auth.oauth_client import github_oauth_client
from src.core.config.settings import get_settings
from src.schemas.v1.user_schemas import UserCreate, UserRead, UserUpdate
from src.core.auth.auth_backend import users

from src.api.v1.team_routes import router as team_router

settings = get_settings()


def include_routes(app: FastAPI) -> None:
    app.include_router(
        users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"]
    )

    app.include_router(
        users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["users"]
    )
    app.include_router(
        users.get_oauth_router(
            github_oauth_client, auth_backend, settings.jwt_secret),
        prefix="/auth/github",
        tags=["auth"]
    )

    app.include_router(
        team_router,
        prefix="/teams",
        tags=["teams"]
    )
