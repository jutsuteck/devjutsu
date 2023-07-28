from typing import List
from src.models.v1.module import Module


class ModuleRepository:
    def __init__(self, session):
        self.session = session

    def add(self, module: Module) -> Module:
        pass

    def filter_by_course(self, course_id: str) -> List[Module]:
        pass

    def get(self, module_id: str) -> Module:
        pass

    def update(self, module_id: str, module_data: dict) -> Module:
        pass

    def delete(self, module: Module) -> None:
        pass
