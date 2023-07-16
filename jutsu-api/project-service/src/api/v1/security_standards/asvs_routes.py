from typing import List
from fastapi import APIRouter

from src.schemas.v1.security_standard.asvs_category_schema import ASVSCategoryReadSchema


router = APIRouter()


""" @router.get('/categories', response_model=List[ASVSCategoryReadSchema]) """
