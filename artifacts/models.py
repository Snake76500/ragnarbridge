"""
Artifact models

Objets produits par les agents
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Artifact:

    name: str

    path: str

    artifact_type: str

    created_by: str = "system"

    created_at: str = None

    size: int = 0


    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.now().isoformat()

