from typing import List
from sqlmodel import Session

from src.models.v1.security_standards.asvs_category import ASVSCategory


class AsvsRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_categories(self) -> List[ASVSCategory]:
        return self.session.query(ASVSCategory).all()

    def get(self, category_id: str) -> ASVSCategory | None:
        return self.session.query(ASVSCategory).get(category_id)
