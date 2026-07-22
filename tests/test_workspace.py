from workspaces.manager import WorkspaceManager


def test_workspace_creation(tmp_path):
    manager = WorkspaceManager(
        base_path=str(tmp_path)
    )

    workspace = manager.create(
        project="demo_ai",
        mission_id="mission_test001"
    )

    assert workspace is not None
    info = workspace.info()
    assert info["id"] == "mission_test001"
    assert info["project"] == "demo_ai"

