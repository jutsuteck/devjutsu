from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.project_routes import router as project_routes
from src.api.v1.workflow_routes import router as workflow_routes

from src.utils.database import init_db


app = FastAPI()

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    project_routes, prefix="/api/v1/projects", tags=["projects"]
)
app.include_router(
    workflow_routes, prefix="/api/v1/workflows", tags=["workflow"]
)


@app.on_event("startup")
def on_startup():
    init_db()
