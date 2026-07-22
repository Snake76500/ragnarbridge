"""
Context Scanner

Découvre automatiquement les artefacts
présents dans un workspace.
"""

from pathlib import Path


class ContextScanner:

    IGNORED_DIRS = {
        "__pycache__",
        ".git",
        ".pytest_cache",
        ".venv",
        ".idea",
        ".vscode"
    }

    IGNORED_EXTENSIONS = {
        ".pyc",
        ".db"
    }

    IGNORED_FILES = {
        ".DS_Store"
    }


    def scan(self, workspace):

        artifacts = []

        for file in workspace.path.rglob("*"):

            if not file.is_file():
                continue

            if self._ignored(file):
                continue

            artifacts.append({

                "name": file.name,

                "path": file,

                "relative_path": file.relative_to(
                    workspace.path
                ),

                "extension": file.suffix,

                "size": file.stat().st_size

            })

        return artifacts


    def _ignored(self, file: Path):

        if any(
            part in self.IGNORED_DIRS
            for part in file.parts
        ):
            return True

        if file.name in self.IGNORED_FILES:
            return True

        if file.suffix in self.IGNORED_EXTENSIONS:
            return True

        return False
