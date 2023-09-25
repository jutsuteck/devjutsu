from fastapi import FastAPI

from src.api.v1.tenant_routes import router as tenant_routes
from src.api.v1.role_routes import router as role_routes
from src.api.v1.clan_routes import router as clan_routes
from src.core.auth.auth_backend import users as fastapi_users
from src.schemas.v1.member_schemas import (
    MemberCreateSchema,
    MemberReadSchema,
    MemberUpdateSchema
)
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
        fastapi_users.get_verify_router(MemberReadSchema),
        prefix="/auth",
        tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix="/auth",
        tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_oauth_router(
            github_oauth_client,
            auth_backend,
            settings.token.oauth_jwt_secret  # type: ignore
        ),
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
        clan_routes,
        prefix="/clans",
        tags=["clans"]
    )
    app.include_router(
        tenant_routes,
        tags=["tenants"]
    )
