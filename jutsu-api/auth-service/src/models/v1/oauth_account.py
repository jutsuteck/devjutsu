from fastapi_users.db import SQLAlchemyBaseOAuthAccountTableUUID
from sqlalchemy import UUID, Column, ForeignKey

from src.models.v1.base import Base


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("member.id"))
