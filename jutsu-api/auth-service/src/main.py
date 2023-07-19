from fastapi import FastAPI

from src.core.dependencies.database.database_manager import database_manager

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await database_manager.create_db_tables()
