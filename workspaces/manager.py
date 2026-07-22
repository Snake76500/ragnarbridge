"""
Workspace Manager

Gestion des espaces de travail
des missions
"""

from pathlib import Path
from datetime import datetime
import uuid

from .models import Workspace


class WorkspaceManager:


    def __init__(
        self,
        base_path="projects"
    ):

        self.base_path = Path(base_path)



    def create(
        self,
        project: str,
        mission_id: str
    ):


        workspace_id = (
            f"{mission_id}"
        )


        path = (
            self.base_path
            / project
            / ".ragnar"
            / "workspaces"
            / workspace_id
        )


        directories = [
            "src",
            "tests",
            "docs",
            "artifacts"
        ]


        for directory in directories:

            (
                path / directory
            ).mkdir(
                parents=True,
                exist_ok=True
            )


        workspace = Workspace(

            id=workspace_id,

            project=project,

            path=path,

            created_at=datetime.now().isoformat()

        )


        return workspace
