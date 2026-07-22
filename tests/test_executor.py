from missions.executor import TaskExecutor
from missions.tasks import Task, TaskStatus
from agents.registry import AgentRegistry


def test_task_executor():
    registry = AgentRegistry()
    executor = TaskExecutor(registry=registry)

    task = Task(
        id=1,
        agent="Développeur Backend",
        description="Créer une API FastAPI"
    )

    result = executor.execute(task)
    assert result.status == TaskStatus.DONE
    assert "Aucun agent trouvé" in result.result

