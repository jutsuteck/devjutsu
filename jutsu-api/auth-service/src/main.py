from fastapi import FastAPI

from src.core.auth.auth_backend import users
from src.core.dependencies.database.database_manager import create_db_and_tables
from src.schemas.v1.user_schemas import UserCreate, UserRead, UserUpdate

app = FastAPI()

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


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
