"""
Mission tasks models
"""

from dataclasses import dataclass, field
from enum import Enum



class TaskStatus(Enum):

    PENDING = "PENDING"

    RUNNING = "RUNNING"

    DONE = "DONE"

    FAILED = "FAILED"



@dataclass
class Task:


    id: int

    agent: str

    description: str

    status: TaskStatus = TaskStatus.PENDING


    result: str | None = None
