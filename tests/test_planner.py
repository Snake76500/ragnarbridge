from adapters.ollama.planner import OllamaPlanner


planner = OllamaPlanner()


plan = planner.create_plan(
    "Créer une API de gestion de stock"
)


print(plan)
