"""
Mission models
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class MissionStatus(Enum):

    CREATED = "CREATED"

    RUNNING = "RUNNING"

    WAITING = "WAITING"

    DONE = "DONE"

    FAILED = "FAILED"



@dataclass
class Mission:

    id: str

    project: str

    goal: str

    status: MissionStatus = MissionStatus.CREATED

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )

    tasks: list = field(
        default_factory=list
    )

@dataclass
class Mission:

    id: str

    project: str

    goal: str

    status: MissionStatus = MissionStatus.CREATED


    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )


    workspace: Optional[object] = None


    tasks: list = field(
        default_factory=list
    )
