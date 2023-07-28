from typing import List
from src.models.v1.course import Course


class CourseRepository:
    def __init__(self, session):
        self.session = session

    def add(self, course: Course) -> Course:
        pass

    def get_all(self) -> List[Course]:
        pass

    def get(self, course_id: str) -> Course:
        pass

    def update(self, course_data: dict) -> Course:
        pass

    def delete(self, course: Course) -> None:
        pass
