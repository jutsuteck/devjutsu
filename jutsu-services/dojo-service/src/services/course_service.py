from typing import List

from fastapi import HTTPException

from src.models.v1.course import Course
from src.repositories.course_repository import CourseRepository


class CourseService:
    def __init__(self, session):
        self.session = session
        self.repository = CourseRepository(self.session)

    def create_course(self, course_data: dict) -> Course:
        course = Course(**course_data)
        return self.repository.add(course)

    def get_all(self) -> List[Course]:
        return self.repository.get_all()

    def get_course_or_404(self, course_id: str) -> Course:
        course = self.repository.get(course_id)

        if not course:
            raise HTTPException(
                status_code=404, detail=f"Course with ({course_id}) not found")

        return course

    def update_course(self, course_id: str, course_data: dict) -> Course:
        course = self.get_course_or_404(course_id)

        """ for key, value in course_data.items(): """
        """     setattr(course, key, value) """

        """ self.repository.update() """

    def delete_course(self, course_id: str) -> None:
        course = self.get_course_or_404(course_id)
        self.repository.delete(course)
