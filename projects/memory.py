"""
Project memory management
"""

from pathlib import Path
import json
import yaml
from datetime import datetime


class ProjectMemory:


    def __init__(self, project_path: Path):

        self.project_path = project_path

        self.ragnar_path = (
            project_path / ".ragnar"
        )

        self.ragnar_path.mkdir(
            exist_ok=True
        )


    def create_metadata(
        self,
        name: str,
        description: str
    ):

        metadata = {

            "name": name,

            "description": description,

            "created": datetime.now().isoformat(),

            "ai": {

                "provider": "antigravity",

                "conversation_id": None
            }
        }


        with open(
            self.ragnar_path / "project.yaml",
            "w",
            encoding="utf-8"
        ) as file:

            yaml.safe_dump(
                metadata,
                file,
                sort_keys=False
            )


    def create_history(self):

        history = []

        with open(
            self.ragnar_path / "history.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=2
            )


    def create_context(self):

        content = """
# Project Context


## Objective




## Architecture decisions


"""

        with open(
            self.ragnar_path / "context.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)


    def initialize(
        self,
        name,
        description
    ):

        self.create_metadata(
            name,
            description
        )

        self.create_history()

        self.create_context()
