from missions.planner import MissionPlanner


def test_mission_planner():
    plan = {
        "architecture": {
            "backend": "FastAPI",
            "database": "PostgreSQL"
        },
        "tasks": [
            {
                "agent": "Database Architect",
                "description": "Créer le schéma PostgreSQL"
            },
            {
                "agent": "Backend Developer",
                "description": "Créer les endpoints REST"
            }
        ]
    }

    planner = MissionPlanner()
    tasks = planner.create_tasks(plan)

    assert len(tasks) == 2
    assert tasks[0].agent == "Database Architect"
    assert tasks[1].agent == "Backend Developer"

