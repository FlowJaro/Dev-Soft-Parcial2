from abc import ABC, abstractmethod
from typing import List, Optional
from model.task import Task
from enums import TaskStatus
from datetime import date

class ITaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task) -> Task:
        ...

    @abstractmethod
    def find_all(self, status: Optional[TaskStatus] = None) -> List[Task]:
        ...

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Task]:
        ...

    @abstractmethod
    def delete(self, id: int) -> None:
        ...

    @abstractmethod
    def find_overdue(self, today: date) -> List[Task]:
        ...
