from fastapi import FastAPI

from src.core.dependencies.database.database_manager import database_manager
from src.core.security.cors import cors_middleware
from src.routes import include_routes


app = FastAPI()

cors_middleware(app)

include_routes(app)


@app.on_event("startup")
def on_startup():
    database_manager.init_db()
