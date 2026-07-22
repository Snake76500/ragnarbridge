from agents.registry import AgentRegistry
from agents.backend_agent import BackendAgent



registry = AgentRegistry()


registry.register(
    "backend",
    BackendAgent()
)



agent = registry.get(
    "backend"
)



print(
    agent.info()
)



class Task:

    description = (
        "Créer une API FastAPI"
    )



result = agent.execute(
    Task()
)


print(result)
