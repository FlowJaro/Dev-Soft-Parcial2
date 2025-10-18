from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class TaskCreateDTO(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    due_date: Optional[date] = None

