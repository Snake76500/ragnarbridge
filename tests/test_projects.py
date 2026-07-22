from unittest.mock import patch
from projects.manager import ProjectManager


def test_project_creation(tmp_path):
    with patch("config.loader.load_config", return_value={"workspace": {"path": str(tmp_path)}}):
        manager = ProjectManager()
        project = manager.create_project(
            "demo_ai",
            "Premier projet généré par RagnarBridge"
        )

        assert project.name == "demo_ai"
        assert "demo_ai" in manager.list_projects()

