from sqlalchemy import UUID, Column, String, text
from sqlalchemy.orm import relationship

from src.models.v1.member import Base


class Permission(Base):
    __tablename__ = "permission"

    id = Column(UUID(as_uuid=True), primary_key=True,
                server_default=text("gen_random_uuid()"))
    name = Column(String, unique=True, nullable=False)
    roles = relationship('Role', secondary="role_permissions",
                         back_populates="permissions")
