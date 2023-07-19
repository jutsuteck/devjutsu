from fastapi import FastAPI

from src.core.dependencies.database.database_manager import create_db_and_tables
from src.routes import include_routes

app = FastAPI()

include_routes(app)


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
