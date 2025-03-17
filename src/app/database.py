from sqlmodel import create_engine

from app.tasks.models import SQLModel
import app.config as config


engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
