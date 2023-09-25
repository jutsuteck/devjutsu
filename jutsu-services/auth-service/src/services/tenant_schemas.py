from typing import List, Optional
from pydantic import BaseModel


class TenantCreateSchema(BaseModel):
    name: str
    member_ids: List[str] = []

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Chatterbot",
                "member_ids": ["member_id1", "member_id2"]
            }
        }


class TenantUpdateSchema(BaseModel):
    name: str


class TenantReadSchema(BaseModel):
    id: str
    name: str
    member_ids: Optional[List[str]]

    class Config:
        from_attributes = True
