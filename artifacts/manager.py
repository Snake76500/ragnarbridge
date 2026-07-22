"""
Artifact Manager

Gestion des productions agents
"""
from typing import List, Union
from .models import Artifact


class ArtifactManager:

    def __init__(self):
        self.items: List[Artifact] = []

    def register(
        self,
        artifact: Union[Artifact, str] = None,
        name: str = None,
        path: str = None,
        artifact_type: str = "other",
        created_by: str = "system",
        size: int = 0
    ) -> Artifact:
        if isinstance(artifact, Artifact):
            item = artifact
        else:
            item = Artifact(
                name=name or (artifact if isinstance(artifact, str) else ""),
                path=path or (artifact if isinstance(artifact, str) else ""),
                artifact_type=artifact_type,
                created_by=created_by,
                size=size
            )

        self.items.append(item)
        return item

    def list(self) -> List[Artifact]:
        return self.items

