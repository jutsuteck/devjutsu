from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "localhost:3000"
    "http://127.0.0.1:3000",
    "https://127.0.0.1:3000",
    "http://localhost:3000",
    "https://localhost:3000",
]


def add_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
