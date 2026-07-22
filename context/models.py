from dataclasses import dataclass, field

from workspaces.models import Workspace
from missions.models import Mission
from .artifact_reader import ArtifactReader
from artifacts.scanner import ArtifactScanner

@dataclass
class AgentContext:

    mission: Mission

    workspace: Workspace

    reader: ArtifactReader = field(
                default_factory=ArtifactReader
    )      

    scanner: ArtifactScanner = field(
        default_factory=ArtifactScanner
    )

    def artifacts(self):
        return self.workspace.artifacts.list()

    def read_artifact(
        self,
        filename
    ):

        return self.reader.read(
            self.workspace,
            filename
        )

    def scan_artifacts(self):
    
        IGNORED_DIRS = {
            "__pycache__",
            ".pytest_cache",
            ".git",
            ".venv"
        }

        IGNORED_EXTENSIONS = {
            ".pyc",
            ".db"
        }

        IGNORED_FILES = {
            ".DS_Store"
        }

        files = []

        for file in self.workspace.path.rglob("*"):

            if file.is_file():

                relative = file.relative_to(
                    self.workspace.path
                )


                if file.suffix == ".py":
                    artifact_type="source"

                elif file.suffix == ".md":
                    artifact_type="documentation"

                elif file.name in [
                    "requirements.txt",
                    "pyproject.toml"
                ]:
                    artifact_type="configuration"

                else:
                    artifact_type="other"
                
                if any(part in IGNORED_DIRS for part in file.parts):
                    continue

                if file.suffix in IGNORED_EXTENSIONS:
                    continue

                if file.name in IGNORED_FILES:
                    continue

                files.append(
                    {
                        "name": file.name,
                        "path": str(relative),
                        "type": artifact_type
                    }
                )


        for artifact in files:

            self.workspace.artifacts.register(
                name=artifact["name"],
                path=artifact["path"],
                artifact_type=artifact["type"]
            )

