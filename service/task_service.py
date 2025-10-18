from typing import List, Optional
from dto.task_create_dto import TaskCreateDTO
from dto.task_dto import TaskDTO
from dto.task_update_status_dto import TaskUpdateStatusDTO
from model.task import Task
from repository.itask_repository import ITaskRepository
from enums import TaskStatus
from datetime import date

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self._repo = repo

    def create(self, dto: TaskCreateDTO) -> TaskDTO:
        # business rules: title required (validated by DTO), default status PENDING
        task = Task(
            id=0,
            title=dto.title.strip(),
            description=dto.description,
            due_date=dto.due_date,
            status=TaskStatus.PENDING
        )
        saved = self._repo.save(task)
        return self._to_dto(saved)

    def list(self, status: Optional[TaskStatus] = None) -> List[TaskDTO]:
        tasks = self._repo.find_all(status=status)
        return [self._to_dto(t) for t in tasks]

    def update_status(self, id: int, dto: TaskUpdateStatusDTO) -> TaskDTO:
        task = self._repo.find_by_id(id)
        if not task:
            raise ValueError(f"Task with id {id} not found")
        # business rule example: cannot move from DONE to other status (example)
        if task.status == TaskStatus.DONE and dto.status != TaskStatus.DONE:
            raise ValueError("Cannot change status of a task already DONE")
        task.status = dto.status
        updated = self._repo.save(task)
        return self._to_dto(updated)

    def delete(self, id: int) -> None:
        task = self._repo.find_by_id(id)
        if not task:
            raise ValueError(f"Task with id {id} not found")
        self._repo.delete(id)

    def list_overdue(self, today: date) -> List[TaskDTO]:
        tasks = self._repo.find_overdue(today)
        return [self._to_dto(t) for t in tasks]

    def _to_dto(self, task: Task) -> TaskDTO:
        return TaskDTO(
            id=task.id,
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            status=task.status
        )
