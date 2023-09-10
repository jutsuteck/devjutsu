from fastapi import FastAPI
from src.core.security.cors import add_middleware

from src.routes import include_routes

app = FastAPI()

add_middleware(app)

include_routes(app)
