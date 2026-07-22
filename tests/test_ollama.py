from adapters.ollama.client import OllamaClient


client = OllamaClient()


response = client.chat(
    """
Tu es un architecte logiciel.
Propose une architecture simple
pour une API de gestion de stock.
"""
)


print(response)
