import uuid

from fastapi_users import schemas
from pydantic import EmailStr


class MemberReadSchema(schemas.BaseUser[uuid.UUID]):
    first_name: str
    last_name: str


class MemberCreateSchema(schemas.BaseUserCreate):
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Clark",
                "last_name": "Kent",
                "email": "clarkkent@superman.com"
            }
        }


class MemberUpdateSchema(schemas.BaseUserUpdate):
    pass