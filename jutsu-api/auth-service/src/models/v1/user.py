from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from src.models.v1.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
