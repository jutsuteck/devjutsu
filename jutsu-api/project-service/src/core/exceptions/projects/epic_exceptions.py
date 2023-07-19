from fastapi import HTTPException


class EpicNotFoundException(HTTPException):
    def __init__(self, epic_id: str, message: str | None = None):
        detail = message or f"Epic with id {epic_id} not found"
        super().__init__(status_code=404, detail=detail)
