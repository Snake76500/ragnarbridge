"""
Agent Registry

Centralise les agents disponibles
"""


class AgentRegistry:


    def __init__(self):

        self.agents = {}
        self.aliases = {}



    def register(
        self,
        key,
        agent,
        aliases=None
    ):

        self.agents[key] = agent


        if aliases:

            for alias in aliases:

                self.aliases[alias] = key



    def get(
        self,
        key
    ):

        real_key = self.aliases.get(
            key,
            key
        )

        return self.agents.get(
            real_key
        )



    def list_agents(self):

        return list(
            self.agents.keys()
        )
