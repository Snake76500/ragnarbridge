"""
Agent Ollama

Utilise un modèle local
"""

from .base import Agent

from adapters.ollama.client import OllamaClient



class OllamaAgent(Agent):


    def __init__(self):

        super().__init__(
            "Ollama"
        )

        self.client = OllamaClient()



    def execute(
        self,
        task
    ):


        prompt = f"""
Tu es un expert logiciel.

Mission :
{task.description}

Explique la solution technique.
"""


        response = self.client.chat(
            prompt
        )


        return response
