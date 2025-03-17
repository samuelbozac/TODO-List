from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.tasks.router import router as tasks_router
from app.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="TODO List API",
    description="",
    docs_url="/docs",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.include_router(
    tasks_router,
    prefix="/tasks",
    tags=["tasks"],
)
