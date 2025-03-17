from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Query,
    HTTPException,
)
from sqlmodel import select

from app.tasks.models import Task
from app.dependencies import SessionDep


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def list_tasks(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Task]:
    tasks = session.exec(select(Task).offset(offset).limit(limit)).all()

    return tasks


@router.get("/{task_id}", status_code=status.HTTP_200_OK)
def get_task(task_id: int, session: SessionDep) -> Task:
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: Task, session: SessionDep) -> Task:
    session.add(task)
    session.commit()
    session.refresh(task)

    return task


@router.put("/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: Task, session: SessionDep):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    task_data = task.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, session: SessionDep) -> dict:
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    session.delete(task)
    session.commit()

    return {"ok": True}
