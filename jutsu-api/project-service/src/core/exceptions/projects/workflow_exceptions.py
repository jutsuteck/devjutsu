from fastapi import HTTPException


class WorklowNotFoundException(HTTPException):
    def __init__(self, workflow_id, message: str | None = None):
        detail = message or f"Workflow with id {workflow_id} not found"
        super().__init__(status_code=404, detail=detail)
