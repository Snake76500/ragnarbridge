"""
Project MCP tools
"""

from projects.manager import ProjectManager


manager = ProjectManager()


def register_project_tools(mcp):

    @mcp.tool()
    def create_project(
        name: str,
        description: str
    ) -> str:
        """
        Create a new project workspace.
        """

        project = manager.create_project(
            name,
            description
        )

        return (
            f"Project created: {project.name}\n"
            f"Path: {project.path}"
        )


    @mcp.tool()
    def list_projects() -> list[str]:
        """
        List available projects.
        """

        return manager.list_projects()
