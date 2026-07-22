from agents.registry import AgentRegistry
from agents.ollama_agent import OllamaAgent



registry = AgentRegistry()



ollama = OllamaAgent()



registry.register(
    "architecte",
    ollama
)



print(
    registry.list_agents()
)



agent = registry.get(
    "architecte"
)



print(
    agent.info()
)
