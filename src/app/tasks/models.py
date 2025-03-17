from sqlmodel import (
    SQLModel,
    Field,
)


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str | None = Field(default=None)
    completed: bool = Field(default=False, index=True)
