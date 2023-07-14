from sqlmodel import SQLModel, Session, create_engine

from src.core.dependencies.database.settings import settings


class DatabaseManager:
    """
    DatabaseManager is a singleton class used for managing database connection. 

    The singleton pattern ensures that only one instance of this class exists. This is beneficial when 
    dealing with database connections, as creating multiple connections can be resource-intensive, 
    and can lead to issues like connection leakage if not properly managed. 

    The DatabaseManager class encapsulates the complexity of connection management by providing 
    methods for getting a database session and initializing the database.

    Attributes:
        _instance: A private class-level attribute to hold the singleton instance.
        _engine: A private instance-level attribute to hold the SQLModel engine.

    Methods:
        __new__(cls): Override to implement the singleton pattern.
        engine: Property that provides access to the SQLModel engine, initializing it if needed.
        get_db(): Provides a database session, managing the context to ensure the session is properly closed.
        init_db(): Initializes the database by creating all tables defined in SQLModel metadata.
    """
    _instance = None
    _engine = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    @property
    def engine(self):
        if self._engine is None:
            DB_USER = settings.postgres_user
            DB_PASSWORD = settings.postgres_password
            DB_NAME = settings.postgres_db
            DB_HOST = settings.postgres_host
            DB_PORT = settings.postgres_port
            DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            self._engine = create_engine(DB_URL, echo=True)

        return self._engine

    def get_db(self):
        with Session(self._engine) as session:
            yield session

    def init_db(self):
        SQLModel.metadata.create_all(self.engine)


database_manager = DatabaseManager()
db_session = database_manager.get_db
