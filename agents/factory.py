"""
Agent Factory

Création automatique des agents
"""

from .backend_agent import BackendAgent
from .antigravity_agent import AntigravityAgent
from .architect_agent import ArchitectAgent


class AgentFactory:


    @staticmethod
    def create(
        role,
        workspace=None
    ):


        role = role.lower()


        if "backend" in role:

            return BackendAgent(
                workspace
            )


        if "architect" in role:

            return ArchitectAgent(
                workspace
            )   
        
        return AntigravityAgent(
            workspace
        )
