from re import A
from typing import List
from fastapi import Depends
from sqlmodel import Session

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.security_standards.asvs_category import ASVSCategory


class ASVSService:
    def __init__(self, session: Session = Depends(db_session)):
        self.session = session
