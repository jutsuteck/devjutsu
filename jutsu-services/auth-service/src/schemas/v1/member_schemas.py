import uuid

from fastapi_users import schemas


class MemberReadSchema(schemas.BaseUser[uuid.UUID]):
    first_name: str
    last_name: str


class MemberCreateSchema(schemas.BaseUserCreate):
    first_name: str
    last_name: str

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Clark",
                "last_name": "Kent",
            }
        }


class MemberUpdateSchema(schemas.BaseUserUpdate):
    pass
