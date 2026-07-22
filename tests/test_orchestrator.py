from missions.orchestrator import MissionOrchestrator



orchestrator = MissionOrchestrator()



mission = orchestrator.create_mission(

    "demo_ai",

    "Créer une API de gestion de stock"

)



print("\nMISSION:")
print(mission)


print("\nTASKS:")


for task in mission.tasks:

    print(
        f"{task.id} - "
        f"{task.agent} : "
        f"{task.description}"
    )
