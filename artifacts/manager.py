"""
Artifact Manager

Gestion des productions agents
"""
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Artifact:

    name: str
    path: str
    relative_path: Path
    extension: str
    size: int

class ArtifactManager:


    def __init__(self):
        self.items = []

    def register(self, artifact):

        # artifact.list
        # artifact = Artifact(
        #     name=name,
        #     path=str(path),
        #     type=artifact_type
        # )

        self.items.append(
            artifact
        )


    def list(self):

        return self.items
