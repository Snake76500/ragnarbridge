from agents.registry import AgentRegistry
from agents.backend_agent import BackendAgent
from missions.tasks import Task


def test_registry_execution():
    registry = AgentRegistry()
    registry.register(
        "backend",
        BackendAgent()
    )

    agent = registry.get("backend")
    assert agent is not None

    task = Task(id=1, agent="backend", description="Créer une API FastAPI")
    result = agent.execute(task)
    assert "Backend Agent exécuté" in result

