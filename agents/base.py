"""
Base Agent

Classe commune à tous les agents RagnarBridge
"""


from abc import ABC, abstractmethod



class Agent(ABC):


    def __init__(
        self,
        name: str,
        capabilities=None
    ):

        self.name = name
        self.capabilities = capabilities or []


    @abstractmethod
    def execute(
        self,
        task,
        workspace=None
    ):

        """
        Exécute une tâche

        Doit être implémenté
        par chaque agent
        """

        pass



    def info(self):

        return {

                "name": self.name,
                "capabilities": self.capabilities

        }
