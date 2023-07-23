from fastapi import HTTPException


class StateNotFoundException(HTTPException):
    def __init__(self, state_id: str, message: str | None = None):
        detail = message or f"State with id {state_id} not found"
        super().__init__(status_code=404, detail=detail)
