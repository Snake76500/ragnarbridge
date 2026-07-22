"""
Mission storage
"""

from pathlib import Path
import yaml


class MissionStorage:


    def __init__(self, path):

        self.path = Path(path)

        self.path.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(self, mission):

        data = {

            "id": mission.id,

            "project": mission.project,

            "goal": mission.goal,

            "status": mission.status.value,

            "created_at": mission.created_at,

            "tasks": [

                {
                    "id": task.id,
                    "agent": task.agent,
                    "description": task.description,
                    "status": task.status.value,
                    "result": task.result
                }

                for task in mission.tasks

            ]        

        }


        filename = (
            self.path /
            f"{mission.id}.yaml"
        )


        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            yaml.safe_dump(
                data,
                file,
                sort_keys=False
            )


    def list(self):

        return list(
            self.path.glob(
                "*.yaml"
            )
        )
