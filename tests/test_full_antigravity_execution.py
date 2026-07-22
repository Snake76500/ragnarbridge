from agents.registry import AgentRegistry
from agents.antigravity_agent import AntigravityAgent
from missions.executor import TaskExecutor
from missions.tasks import Task
from pathlib import Path


registry = AgentRegistry()


antigravity = AntigravityAgent(
    workspace="/home/fabien/ragnarlab/projects/demo_ai/workspaces/test1"
)

registry.register(
    "developer",
    antigravity,
    aliases=[
        "Développeur Backend",
        "Backend Developer"
    ]
)

workspace = Path(
    "/home/fabien/ragnarlab/projects/demo_ai/workspaces/test1"
)


executor = TaskExecutor(
    registry,
    workspace
)


task = Task(
        id=1,
        agent="Architecte Logiciel",
        description="""
        Concevoir l'architecture d'une API
        de gestion de stock.
        """
)



result = executor.execute(
    task
)


print(result)
