"""
Mission Orchestrator

Coordonne :
- création mission
- planification Ollama
- génération des tâches
"""


from .manager import MissionManager
from .planner import MissionPlanner

from adapters.ollama.planner import OllamaPlanner
from workspaces.manager import WorkspaceManager


class MissionOrchestrator:


    def __init__(self):

        self.mission_manager = MissionManager()

        self.workspace_manager = WorkspaceManager(
            base_path="/home/fabien/ragnarlab/projects"
        )

        self.ollama_planner = OllamaPlanner()

        self.task_planner = MissionPlanner()


    def create_mission(
        self,
        project: str,
        goal: str
    ):


        #
        # 1 - Création mission initiale
        #

        mission = self.mission_manager.create_mission(

            project,

            goal

        )

        #
        # 2 - Création workspace
        #

        workspace = self.workspace_manager.create(

            project,

            mission.id

        )


        mission.workspace = workspace


        #
        # 3 - Génération plan avec Ollama
        #

        plan = self.ollama_planner.create_plan(

            goal

        )


        #
        # 4 - Conversion plan en Tasks
        #

        mission.tasks = (

            self.task_planner.create_tasks(

                plan

            )

        )


        #
        # 5 - Mise à jour future
        #
        # La persistance complète sera ajoutée
        # avec le MissionRepository

        return mission
