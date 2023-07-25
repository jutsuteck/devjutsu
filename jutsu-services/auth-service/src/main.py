from fastapi import FastAPI

from src.routes import include_routes

app = FastAPI()

include_routes(app)
