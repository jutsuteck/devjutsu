from sqlmodel import SQLModel, Session, create_engine

from src.utils.settings import settings


DB_USER = settings.postgres_user
DB_PASSWORD = settings.postgres_password
DB_NAME = settings.postgres_db
DB_HOST = settings.postgres_host
DB_PORT = settings.postgres_port

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL, echo=True)


def db_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
