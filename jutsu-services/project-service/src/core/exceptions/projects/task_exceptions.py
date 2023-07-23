from fastapi import HTTPException


class TaskNotFoundException(HTTPException):
    def __init__(self, task_id: str, message: str | None = None):
        detail = message or f"Task with id {task_id} not found"
        super().__init__(status_code=404, detail=detail)
