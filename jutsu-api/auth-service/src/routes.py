from fastapi import FastAPI

from src.api.v1.role_routes import router as role_routes
from src.api.v1.team_routes import router as team_routes
from src.core.auth.auth_backend import users as fastapi_users
from src.schemas.v1.member_schemas import MemberCreateSchema, MemberReadSchema, MemberUpdateSchema
from src.core.config.settings import get_settings

from src.core.auth.auth_backend import auth_backend
from src.core.auth.oauth_client import github_oauth_client


settings = get_settings()


def include_routes(app: FastAPI) -> None:
    app.include_router(
        fastapi_users.get_register_router(
            MemberReadSchema, MemberCreateSchema),
        prefix="/auth",
        tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix="/auth/jwt",
        tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_oauth_router(
            github_oauth_client, auth_backend, settings.jwt_secret),
        prefix="/auth/github",
        tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_users_router(MemberReadSchema, MemberUpdateSchema),
        prefix="/users",
        tags=["users"]
    )
    app.include_router(
        role_routes,
        prefix="/roles",
        tags=["roles"]
    )
    app.include_router(
        team_routes,
        prefix="/teams",
        tags=["teams"]
    )
