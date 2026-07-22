from agents.registry import AgentRegistry
from agents.antigravity_agent import AntigravityAgent
from missions.tasks import Task

registry = AgentRegistry()


antigravity = AntigravityAgent()


registry.register(
    "developer",
    antigravity
)


print("Agents :")
print(registry.list_agents())


agent = registry.get(
    "developer"
)


task = Task(
    id=1,
    agent="developer",
    description="Créer une fonction Python qui calcule la TVA"
)


print("\nExecution :")

result = agent.execute(task)


print(result)
