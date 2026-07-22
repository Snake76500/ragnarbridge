from unittest.mock import MagicMock
from missions.orchestrator import MissionOrchestrator


def test_mission_orchestrator(tmp_path):
    orchestrator = MissionOrchestrator(base_path=str(tmp_path))
    orchestrator.ollama_planner.create_plan = MagicMock(return_value={
        "tasks": [
            {"agent": "Architect", "description": "Design system"}
        ]
    })

    mission = orchestrator.create_mission(
        "demo_ai",
        "Créer une API de gestion de stock"
    )

    assert mission is not None
    assert mission.workspace is not None
    assert len(mission.tasks) == 1

