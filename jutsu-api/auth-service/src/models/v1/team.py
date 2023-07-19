from sqlalchemy import UUID, Column, String, text
from src.models.v1.base import Base


class Team(Base):
    __tablename__ = "team"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, index=True)
