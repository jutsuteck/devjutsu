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
        workflow_routes, prefix="/api/v1/workflows", tags=["workflow"]
    )
    app.include_router(
        epic_routes, prefix="/api/v1/epics", tags=["epics"]
    )
    app.include_router(
        state_routes, prefix="/api/v1/states", tags=["states"]
    )
    app.include_router(
        work_item_routes, prefix="/api/v1/work_items", tags=["work items"]
    )
    app.include_router(
        task_routes, prefix="/api/v1/tasks", tags=["tasks"]
    )
    app.include_router(
        label_routes, prefix="/api/v1/labels", tags=["labels"]
    )
