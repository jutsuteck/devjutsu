from pydantic import BaseModel


class ASVSRequirementReadSchema(BaseModel):
    id: str
    requirement_id: str
    description: str
    objective: str
    value: str

    class Config:
        orm_mode = True
