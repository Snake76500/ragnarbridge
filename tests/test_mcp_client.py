import asyncio
import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


@pytest.mark.skip(reason="Manual integration test requiring active MCP server")
@pytest.mark.asyncio
async def test_mcp_client():
    server_params = StdioServerParameters(
        command="python",
        args=[
            "-m",
            "mcp_server.server"
        ]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            assert len(tools.tools) > 0

