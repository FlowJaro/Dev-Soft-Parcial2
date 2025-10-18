from pydantic import BaseModel
from datetime import date
from typing import Optional
from enums import TaskStatus

class TaskDTO(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus
