from agents.registry import AgentRegistry
from agents.antigravity_agent import AntigravityAgent
from missions.executor import TaskExecutor
from missions.tasks import Task
from pathlib import Path
from workspaces.manager import WorkspaceManager
from context.models import AgentContext
from missions.models import Mission


# 1 - Création mission

mission = Mission(

    id="mission_test001",

    project="demo_ai",

    goal="Créer une API REST FastAPI"

)

# 2 - Création workspace

workspace_manager = WorkspaceManager(
    "projects"
)


workspace = workspace_manager.create(
    "demo_ai",
    mission.id
)


# 3 - Création contexte agent

context = AgentContext(

    mission=mission,

    workspace=workspace

)

context = AgentContext(
    mission=mission,
    workspace=workspace
)


registry = AgentRegistry()


antigravity = AntigravityAgent(
    workspace="/home/fabien/ragnarlab/projects/demo_ai/workspaces/test1"
)

registry.register(
    "architect",
    AntigravityAgent()
)

workspace_manager = WorkspaceManager(
    "/home/fabien/ragnarlab/projects"
)


workspace = workspace_manager.create(
    "demo_ai",
    "test1"
)

executor = TaskExecutor(
    registry,
    context 
)


task = Task(
        id=1,
        agent="architect",
        description="""
        Concevoir l'architecture d'une API
        de gestion de stock.
        """
)



result = executor.execute(
    task
)


print(result)
print("\nARTIFACTS:")

for artifact in context.workspace.artifacts.list():

    print(
        f"- {artifact.type}: {artifact.path}"
    )
