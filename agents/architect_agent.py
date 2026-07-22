"""
Architect Agent

Agent spécialisé architecture logicielle
"""

from .antigravity_agent import AntigravityAgent
from artifacts.models import Artifact


class ArchitectAgent(AntigravityAgent):


    def __init__(
        self,
        workspace=None
    ):

        super().__init__(
            workspace
        )

        self.name = "architect"

        self.capabilities = [
            "software architecture",
            "system design",
            "database design",
            "api design",
            "documentation"
        ]



    def execute(
        self,
        task,
        workspace=None
    ):


        original_description = task.description


        task.description = f"""
Tu es un Architecte Logiciel senior.

Tes responsabilités :

- analyser les besoins fonctionnels
- définir une architecture propre
- choisir les technologies adaptées
- définir les composants du système
- définir le modèle de données
- définir les APIs nécessaires

Tu dois produire de la documentation technique.

Crée obligatoirement dans le workspace :

docs/
├── architecture.md
├── database-design.md
└── api-spec.md


Sujet :

{original_description}


Contraintes :

- Ne génère pas uniquement une réponse texte.
- Crée les fichiers dans le workspace.
- Utilise une documentation professionnelle.
- Explique les choix techniques.
"""


        result = super().execute(
            task,
            workspace
        )

        if workspace:
            ws_obj = getattr(workspace, "workspace", workspace)
            if hasattr(ws_obj, "artifacts"):
                ws_obj.artifacts.register(
                    Artifact(
                        name="architecture.md",
                        path="docs/architecture.md",
                        artifact_type="documentation",
                        created_by=self.name
                    )
                )

        return result

