import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=[
            "-m",
            "server.main"
        ]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Tools disponibles:")

            for tool in tools.tools:
                print("-", tool.name)

            result = await session.call_tool(
                "generate_code",
                {
                    "prompt": "Crée une fonction Python qui additionne deux nombres"
                }
            )

            print("\nRéponse:")
            print(result)

            result = await session.call_tool(
                "list_projects",
                {}
            )

            print("\nProjects:")
            print(result)

            result = await session.call_tool(
                "create_mission",
                {
                    "project": "demo_ai",
                    "goal": "Créer une application FastAPI complète"
                }
            )

            print("\nMission:")
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
