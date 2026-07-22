from missions.manager import MissionManager


def test_mission_creation(tmp_path):
    storage_path = str(tmp_path / "missions")
    manager = MissionManager(storage_path)

    mission = manager.create_mission(
        "demo_ai",
        "Créer une API REST FastAPI"
    )

    assert mission is not None
    assert mission.project == "demo_ai"
    assert len(manager.list_missions()) == 1

