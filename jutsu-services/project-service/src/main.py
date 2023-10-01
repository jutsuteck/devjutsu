from fastapi import FastAPI

from src.core.dependencies.database.database_manager import database_manager
from src.core.security.cors import cors_middleware
from src.core.utils.seed_asvs_data import seed_data_to_db
from src.routes import include_routes


app = FastAPI()

cors_middleware(app)

include_routes(app)


@app.on_event("startup")
def on_startup():
    database_manager.init_db()
    seed_data_to_db("src/core/utils/asvs_data.json")
