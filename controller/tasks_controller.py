from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from dto.task_create_dto import TaskCreateDTO
from dto.task_update_status_dto import TaskUpdateStatusDTO
from dto.task_dto import TaskDTO
from enums import TaskStatus
from service.task_service import TaskService
from repository.inmemory_task_repository import InMemoryTaskRepository
from datetime import date

router = APIRouter(prefix="/tasks", tags=["tasks"])

_repo = InMemoryTaskRepository()
_service = TaskService(_repo)

def handle_service_call(func):
    try:
        return func()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_service():
    return _service

@router.post("", response_model=TaskDTO, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreateDTO, service: TaskService = Depends(get_service)):
    return handle_service_call(lambda: service.create(payload))

@router.get("", response_model=List[TaskDTO])
def list_tasks(
    status: Optional[TaskStatus] = Query(None),
    service: TaskService = Depends(get_service)
):
    return handle_service_call(lambda: service.list(status=status))

@router.patch("/{id}/status", response_model=TaskDTO)
def update_status(id: int, payload: TaskUpdateStatusDTO, service: TaskService = Depends(get_service)):
    return handle_service_call(lambda: service.update_status(id, payload))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, service: TaskService = Depends(get_service)):
    return handle_service_call(lambda: service.delete(id))

@router.get("/overdue", response_model=List[TaskDTO])
def get_overdue(today: Optional[date] = None, service: TaskService = Depends(get_service)):
    t = today or date.today()
    return handle_service_call(lambda: service.list_overdue(t))

