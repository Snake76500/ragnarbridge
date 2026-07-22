from workspaces.manager import WorkspaceManager


manager = WorkspaceManager(
    base_path="/home/fabien/ragnarlab/projects"
)


workspace = manager.create(
    project="demo_ai",
    mission_id="mission_test001"
)


print(workspace)

print(workspace.info())
