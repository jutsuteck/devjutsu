from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.security_standard.asvs_category_schema import ASVSCategoryReadSchema
from src.services.security_standards.asvs_service import ASVSService


router = APIRouter(prefix="/api/v1/asvs")


@router.get('/categories', response_model=List[ASVSCategoryReadSchema])
def category_list(service: ASVSService = Depends(ASVSService)):
    return service.get_all_categories()
