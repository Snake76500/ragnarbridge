"""
Mission MCP tools
"""

from missions.manager import MissionManager


manager = MissionManager()



def register_mission_tools(mcp):


    @mcp.tool()
    def create_mission(
        project: str,
        goal: str
    ) -> str:
        """
        Create a new mission.
        """

        mission = manager.create_mission(
            project,
            goal
        )


        return (
            f"Mission created\n"
            f"ID: {mission.id}\n"
            f"Project: {mission.project}\n"
            f"Goal: {mission.goal}"
        )



    @mcp.tool()
    def list_missions() -> list[str]:
        """
        List active missions.
        """


        return [

            (
                f"{m.id} - "
                f"{m.goal}"
            )

            for m in manager.list_missions()

        ]
