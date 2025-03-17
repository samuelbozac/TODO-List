import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session
from sqlalchemy_utils import database_exists, create_database

from main import app
from app.config import SQLALCHEMY_TEST_DATABASE_URL
from app.tasks.models import SQLModel
from app.dependencies import get_session


engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)


def override_get_session():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = override_get_session

client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_db():
    # Check if the test database exists, if not create it
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Database not found, created!")

    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    yield

    SQLModel.metadata.drop_all(engine)
