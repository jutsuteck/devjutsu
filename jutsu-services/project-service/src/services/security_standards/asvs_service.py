from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.security_standards.asvs_category import ASVSCategory
from src.repositories.security_standards.asvs_repository import AsvsRepository


class ASVSService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
        self.asvs_repository = AsvsRepository(self.session)

    def get_all_categories(self) -> List[ASVSCategory]:
        return self.asvs_repository.get_all_categories()

    def get_category_or_404(self, category_id: str) -> ASVSCategory:
        category = self.asvs_repository.get(category_id)

        if not category:
            raise HTTPException(status_code=404, detail="Not found")

        return category
