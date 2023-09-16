from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def cors_middleware(app: FastAPI):
    origins = [
        "192.168.207.41",
        "http://auth_service:8000"
        "localhost:3000",
        "http://127.0.0.1:3000",
        "https://127.0.0.1:3000",
        "http://localhost:3000",
        "https://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
