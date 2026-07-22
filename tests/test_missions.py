from missions.manager import MissionManager


manager = MissionManager(
    "/home/fabien/ragnarlab/projects/demo_ai/.ragnar/missions"
)


mission = manager.create_mission(
    "demo_ai",
    "Créer une API REST FastAPI"
)


print("Mission créée:")
print(mission)


print("\nListe missions:")
print(
    manager.list_missions()
)
