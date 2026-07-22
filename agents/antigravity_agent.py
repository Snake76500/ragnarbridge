"""
Antigravity Agent

Agent exécutant les tâches via Gemini
à travers le CLI Antigravity.
"""

from agents.base import Agent
from adapters.antigravity.client import AntigravityClient


class AntigravityAgent(Agent):


    def __init__(
        self,
        workspace=None
    ):
        super().__init__(
            "antigravity"
        )
        self.workspace = workspace

        self.client = AntigravityClient(
            workspace=workspace
        )

    def execute(self, task, workspace=None):

        current_workspace = (
            workspace
            or self.workspace
        )

        ws_obj = getattr(current_workspace, "workspace", current_workspace)
        workspace_path = (
            ws_obj.path
            if hasattr(ws_obj, "path")
            else ws_obj
        )

        prompt = f"""
        Tu es un développeur logiciel expert.

        Tu travailles dans le workspace :

        {workspace_path or "aucun workspace défini"}

        Tu dois réaliser la tâche suivante :

        {task.description}

        Contraintes :
        - IMPORTANT :
            Tu dois créer réellement les fichiers dans le répertoire courant.
            Ne crée aucun fichier dans :
            - ~/.gemini
            - scratch
            - /tmp
            Le workspace courant est le seul emplacement autorisé.
        - Respecte une architecture propre.
        - Implémente réellement la solution.
        - Fournis un résumé des fichiers créés.
        """

        result = self.client.generate(
            prompt,
            workspace=ws_obj
        )

        if result.success:

            return (
                "Antigravity Agent exécuté :\n\n"
                + result.output
            )

        return (
            "Erreur Antigravity : "
            + str(result.error)
        )
