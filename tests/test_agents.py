from agents.registry import AgentRegistry
from agents.ollama_agent import OllamaAgent


def test_agent_registry():
    registry = AgentRegistry()
    ollama = OllamaAgent()

    registry.register(
        "architecte",
        ollama
    )

    assert "architecte" in registry.list_agents()
    agent = registry.get("architecte")
    assert agent is not None
    info = agent.info()
    assert "name" in info

