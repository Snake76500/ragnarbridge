from agents.registry import AgentRegistry
from agents.antigravity_agent import AntigravityAgent
from missions.executor import TaskExecutor
from missions.tasks import Task, TaskStatus
from workspaces.manager import WorkspaceManager
from context.models import AgentContext
from missions.models import Mission


def test_full_antigravity_execution(tmp_path):
    mission = Mission(
        id="mission_test001",
        project="demo_ai",
        goal="Créer une API REST FastAPI"
    )

    workspace_manager = WorkspaceManager(str(tmp_path))
    workspace = workspace_manager.create("demo_ai", mission.id)

    context = AgentContext(
        mission=mission,
        workspace=workspace
    )

    registry = AgentRegistry()
    registry.register("architect", AntigravityAgent())

    executor = TaskExecutor(registry, context)
    task = Task(
        id=1,
        agent="architect",
        description="Concevoir l'architecture d'une API de gestion de stock."
    )

    result = executor.execute(task)
    assert result.status == TaskStatus.DONE

if __name__ == "__main__":
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as tmpdir:
        test_full_antigravity_execution(Path(tmpdir))
        print("Test exécuté avec succès !")