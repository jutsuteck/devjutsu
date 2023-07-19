from fastapi import HTTPException


class LabelNotFoundException(HTTPException):
    def __init__(self, label_id: str, message: str | None = None):
        detail = message or f"Label with id {label_id} not found"
        super().__init__(status_code=404, detail=detail)
