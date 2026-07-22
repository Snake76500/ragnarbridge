"""
Workspace models

Définit les espaces de travail
des missions RagnarBridge
"""

from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
from artifacts.manager import ArtifactManager

@dataclass
class Workspace:

    id: str

    project: str

    path: Path

    created_at: str
    
    artifacts: ArtifactManager = field(
    default_factory=ArtifactManager
    )   

    def info(self):

        return {
            "id": self.id,
            "project": self.project,
            "path": str(self.path),
            "created_at": self.created_at
        }
