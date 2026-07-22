"""
Backend Agent

Agent spécialisé développement backend
"""

from .antigravity_agent import AntigravityAgent


class BackendAgent(AntigravityAgent):


    def __init__(
        self,
        workspace=None
    ):

        super().__init__(
            workspace
        )

        self.name = "backend"

        self.capabilities = [
            "python",
            "fastapi",
            "api",
            "database",
            "sql"
        ]


    def execute(
        self,
        task,
        workspace=None
    ):


        original_description = task.description


        task.description = f"""
Tu es un développeur Backend senior.

Compétences :
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- API REST
- Architecture propre

Tu dois réaliser :

{original_description}

Consignes :
- Crée directement les fichiers dans le workspace.
- Produit du code réellement exploitable.
- Respecte les bonnes pratiques professionnelles.
"""


        return super().execute(
            task,
            workspace
        )
