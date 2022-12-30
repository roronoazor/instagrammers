import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import get_db
from app.main import app
from app.models import Base

DATABASE_URL = "sqlite:///./test.sqlite3"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)


def get_test_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module", name="client")
def test_app():
    # Create tables for testing only
    Base.metadata.create_all(engine)

    app.dependency_overrides[get_db] = get_test_db
    client = TestClient(app)
    yield client

    # Drop tables when testing is finished
    Base.metadata.drop_all(engine)  # comment this line to persist test data
