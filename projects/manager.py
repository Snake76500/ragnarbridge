"""
Project Manager
"""

from pathlib import Path

from .models import Project

from .memory import ProjectMemory

class ProjectManager:

    def __init__(self):

        from config.loader import load_config

        config = load_config()

        workspace = config["workspace"]["path"]

        self.workspace = Path(workspace)

    def create_project(
        self,
        name: str,
        description: str
    ) -> Project:

        project_path = self.workspace / name

        project_path.mkdir(
            parents=True,
            exist_ok=True
        )

        ragnar_dir = project_path / ".ragnar"

        ragnar_dir.mkdir(
            exist_ok=True
        )

        project = Project(
            name=name,
            description=description,
            path=project_path
        )

        memory = ProjectMemory(
            project_path
        )

        memory.initialize(
            name,
            description
        )

        return project


    def list_projects(self):

        return [
            p.name
            for p in self.workspace.iterdir()
            if p.is_dir()
        ]
