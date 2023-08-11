from pydantic import BaseModel


class PermissionReadSchema(BaseModel):
    name: str
