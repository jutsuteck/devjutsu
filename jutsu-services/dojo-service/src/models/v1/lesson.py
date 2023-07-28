from sqlmodel import SQLModel


class Lesson(SQLModel, table=True):
    pass
