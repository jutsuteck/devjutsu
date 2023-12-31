from typing import List
from fastapi import APIRouter, Depends
from src.core.security.auth import get_current_user

from src.schemas.v1.projects.label_schema import LabelCreateSchema, LabelReadSchema, LabelUpdateSchema
from src.services.projects.label_service import LabelService


router = APIRouter(prefix="/api/v1")


@router.post("/labels/new", response_model=LabelReadSchema)
def label_create(
        work_item_id: str,
        label_create_schema: LabelCreateSchema,
        service: LabelService = Depends(LabelService),
        current_user=Depends(get_current_user)):
    return service.create_work_item_label(
        work_item_id, label_create_schema.dict())


@router.get('/labels/all/{work_item_id}', response_model=List[LabelReadSchema])
def label_list(
        work_item_id: str,
        service: LabelService = Depends(LabelService),
        current_user=Depends(get_current_user)):
    return service.filter_by_work_item(work_item_id)


@router.patch('/labels/update/{label_id}', response_model=LabelReadSchema)
def label_update(
        label_id: str,
        label_update_schema: LabelUpdateSchema,
        service: LabelService = Depends(LabelService),
        current_user=Depends(get_current_user)):
    return service.update_label(label_id, label_update_schema.name)


@router.delete('/labels/delete/{label_id}')
def label_delete(
        label_id: str,
        service: LabelService = Depends(LabelService),
        current_user=Depends(get_current_user)):
    return service.delete_label(label_id)
