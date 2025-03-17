from dotenv import load_dotenv
from pathlib import Path
import os

BASE_PATH = Path().parent.parent.resolve()

load_dotenv(
    f"{BASE_PATH}/.env",
)

DEBUG = True

database = {
    "POSTGRES_DB": os.getenv("POSTGRES_DB", "todolist"),
    "POSTGRES_USER": os.getenv("POSTGRES_USER", "root"),
    "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD", "root"),
    "POSTGRES_HOST": os.getenv("POSTGRES_HOST", "db"),
    "POSTGRES_PORT": os.getenv("POSTGRES_PORT", "5432"),
}

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    database.get("POSTGRES_USER"),
    database.get("POSTGRES_PASSWORD"),
    "db" if DEBUG else database.get("POSTGRES_HOST"),
    database.get("POSTGRES_DB"),
)

SQLALCHEMY_TEST_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    database.get("POSTGRES_USER"),
    database.get("POSTGRES_PASSWORD"),
    "db" if DEBUG else database.get("POSTGRES_HOST"),
    database.get("POSTGRES_DB") + "_test",
)
