from typing import List
from fastapi import APIRouter, Depends

from src.schemas.v1.projects.label_schema import LabelCreateSchema, LabelReadSchema, LabelUpdateSchema
from src.services.projects.label_service import LabelService


router = APIRouter()


@router.post("/new", response_model=LabelReadSchema)
def label_create(work_item_id: str, label_create_schema: LabelCreateSchema, service: LabelService = Depends(LabelService)):
    return service.create_work_item_label(
        work_item_id, label_create_schema.dict())


@router.get('/all/{work_item_id}', response_model=List[LabelReadSchema])
def label_list(work_item_id: str, service: LabelService = Depends(LabelService)):
    return service.get_all_work_item_labels(work_item_id)


@router.patch('/update/{label_id}', response_model=LabelReadSchema)
def label_update(label_id, label_update_schema: LabelUpdateSchema, service: LabelService = Depends(LabelService)):
    return service.update_label(label_id, label_update_schema.name)


@router.delete('/delete/{label_id}')
def label_delete(label_id: str, service: LabelService = Depends(LabelService)):
    return service.delete_label(label_id)
