"""
Project models
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Project:

    name: str
    description: str
    path: Path
    conversation_id: str | None = None
