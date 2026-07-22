from agents.registry import AgentRegistry
from agents.antigravity_agent import AntigravityAgent
from missions.tasks import Task


def test_antigravity_agent_registration():
    registry = AgentRegistry()
    antigravity = AntigravityAgent()

    registry.register(
        "developer",
        antigravity
    )

    assert "developer" in registry.list_agents()
    agent = registry.get("developer")
    assert agent is not None
    assert agent.name == "antigravity"

