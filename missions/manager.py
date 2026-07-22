"""
Mission manager
"""

import uuid
from pathlib import Path

from .models import Mission
from .storage import MissionStorage
from .tasks import Task


class MissionManager:


    def __init__(
        self,
        storage_path=None
    ):

        if storage_path is None:

            storage_path = (
                "./.ragnar/missions"
            )


        self.storage = MissionStorage(
            storage_path
        )


        self.missions = {}



    def create_mission(
        self,
        project: str,
        goal: str
    ):


        mission_id = (
            "mission_"
            + str(uuid.uuid4())[:8]
        )


        mission = Mission(

            id=mission_id,

            project=project,

            goal=goal,

            tasks=[

               Task(
                    id=1,
                     agent="Architecte Logiciel",
                    description="Analyser le besoin et définir l'architecture"
                    ),

                Task(
                    id=2,
                    agent="Développeur Backend",
                    description="Créer l'API backend"
                ),

                Task(
                    id=3,
                    agent="Développeur Frontend",
                    description="Créer l'interface utilisateur"
                ),

                Task(
                    id=4,
                    agent="QA",
                    description="Créer les tests"
                )

            ]

        )


        self.missions[
            mission_id
        ] = mission


        self.storage.save(
            mission
        )


        return mission



    def list_missions(self):

        return list(
            self.missions.values()
        )
