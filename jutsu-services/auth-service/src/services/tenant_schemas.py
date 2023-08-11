from pydantic import BaseModel


class TenantCreateSchema(BaseModel):
    name: str

    json_schema_extra = {
        "example": {
            "name": "Chatterbot"
        }
    }


class TenantUpdateSchema(BaseModel):
    name: str


class TenantReadSchema(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True
