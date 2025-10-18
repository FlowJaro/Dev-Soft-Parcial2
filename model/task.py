from dataclasses import dataclass
from datetime import date
from typing import Optional
from enums import TaskStatus

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[date]
    status: TaskStatus = TaskStatus.PENDING
