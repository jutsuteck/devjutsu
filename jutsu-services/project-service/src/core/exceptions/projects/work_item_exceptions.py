from fastapi import HTTPException


class WorkItemNotFoundException(HTTPException):
    def __init__(self, work_item_id: str, message: str | None = None):
        detail = message or f"Work item with id {work_item_id} not found"
        super().__init__(status_code=404, detail=detail)
