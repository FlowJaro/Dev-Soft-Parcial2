from typing import List, Optional
from model.task import Task
from datetime import date
from enums import TaskStatus
from .itask_repository import ITaskRepository

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._store: List[Task] = []
        self._next_id = 1

    def _generate_id(self) -> int:
        nid = self._next_id
        self._next_id += 1
        return nid

    def save(self, task: Task) -> Task:
        if task.id == 0:
            task.id = self._generate_id()
            self._store.append(task)
        else:
            # update existing
            for i, t in enumerate(self._store):
                if t.id == task.id:
                    self._store[i] = task
                    break
        return task

    def find_all(self, status: Optional[TaskStatus] = None) -> List[Task]:
        if status:
            return [t for t in self._store if t.status == status]
        return list(self._store)

    def find_by_id(self, id: int) -> Optional[Task]:
        for t in self._store:
            if t.id == id:
                return t
        return None

    def delete(self, id: int) -> None:
        self._store = [t for t in self._store if t.id != id]

    def find_overdue(self, today: date) -> List[Task]:
        # overdue = due_date < today and not DONE
        res = []
        for t in self._store:
            if t.due_date and t.due_date < today and t.status != TaskStatus.DONE:
                res.append(t)
        return res
