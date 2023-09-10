import uuid

from fastapi_users import schemas


class MemberReadSchema(schemas.BaseUser[uuid.UUID]):
    pass


class MemberCreateSchema(schemas.BaseUserCreate):

    class Config:
        json_schema_extra = {
            "example": {
                "email": "clarkkent@email.com",
                "password": "iamavalidpassword"
            }
        }


class MemberUpdateSchema(schemas.BaseUserUpdate):
    pass
