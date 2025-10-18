from pydantic import BaseModel
from enums import TaskStatus

class TaskUpdateStatusDTO(BaseModel):
    status: TaskStatus
