"""
RagnarBridge MCP Server
"""

from mcp.server.fastmcp import FastMCP

from adapters.antigravity.client import AntigravityClient

from mcp_server.tools.projects import register_project_tools

from mcp_server.tools.missions import register_mission_tools


mcp = FastMCP(
    "RagnarBridge"
)


antigravity = AntigravityClient()


@mcp.tool()
def generate_code(prompt: str) -> str:
    """
    Generate code using Antigravity.
    """

    res = antigravity.generate(prompt)
    if res.success:
        return res.output
    return f"Error: {res.error}"



register_project_tools(mcp)
register_mission_tools(mcp)


if __name__ == "__main__":
    mcp.run()
