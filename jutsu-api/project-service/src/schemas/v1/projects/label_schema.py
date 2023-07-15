from pydantic import BaseModel


class LabelCreateSchema(BaseModel):
    name: str
    work_item_id: str

    class Config:
        schema_extra = {
            "example": {
                "name": "UI",
                "work_item_item": "{work_item_id}"
            }
        }


class LabelUpdateSchema(BaseModel):
    name: str


class LabelReadSchema(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
