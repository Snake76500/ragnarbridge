from agents.registry import AgentRegistry
from agents.backend_agent import BackendAgent

from missions.executor import TaskExecutor

from missions.tasks import Task



registry = AgentRegistry()


registry.register(
    "backend",
    BackendAgent()
)



executor = TaskExecutor(
    registry
)



task = Task(

    id=1,

    agent="backend",

    description=
    "Créer une API FastAPI"

)



result = executor.execute(
    task
)


print(result)

print(
    result.status
)

print(
    result.result
)
