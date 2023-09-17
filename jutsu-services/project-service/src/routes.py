from fastapi import FastAPI
from src.api.v1.projects.project_routes import router as project_routes
from src.api.v1.projects.epic_routes import router as epic_routes
from src.api.v1.projects.workflow_routes import router as workflow_routes
from src.api.v1.projects.state_routes import router as state_routes
from src.api.v1.projects.work_item_routes import router as work_item_routes
from src.api.v1.projects.task_routes import router as task_routes
from src.api.v1.projects.label_routes import router as label_routes


def include_routes(app: FastAPI) -> None:
    app.include_router(
        project_routes, tags=["projects"]
    )
    app.include_router(
        workflow_routes, tags=["workflow"]
    )
    app.include_router(
        epic_routes, tags=["epics"]
    )
    app.include_router(
        state_routes, tags=["states"]
    )
    app.include_router(
        work_item_routes, tags=["work items"]
    )
    app.include_router(
        task_routes, tags=["tasks"]
    )
    app.include_router(
        label_routes, tags=["labels"]
    )
