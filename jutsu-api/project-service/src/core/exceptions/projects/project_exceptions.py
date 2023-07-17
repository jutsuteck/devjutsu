from fastapi import HTTPException


class ProjectNotFoundException(HTTPException):
    def __init__(self, project_id: str, message: str | None = None):
        detail = message or f"Project with ID {project_id} not found"
        super().__init__(status_code=404, detail=detail)


class IncorrectProjectNameKeyException(HTTPException):
    def __init__(self, name_key: str, message: str | None = None):
        detail = message or f"Project with name key \"{name_key}\""
        super().__init__(status_code=404, detail=detail)
