from agents.registry import AgentRegistry
from agents.backend_agent import BackendAgent
from missions.executor import TaskExecutor
from missions.tasks import Task, TaskStatus


def test_full_execution():
    registry = AgentRegistry()
    registry.register(
        "backend",
        BackendAgent()
    )

    executor = TaskExecutor(registry)
    task = Task(
        id=1,
        agent="backend",
        description="Créer une API FastAPI"
    )

    result = executor.execute(task)
    assert result.status == TaskStatus.DONE
    assert "Backend Agent exécuté" in result.result

