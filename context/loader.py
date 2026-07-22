from .models import AgentContext


class ContextLoader:


    def build(
        self,
        mission,
        workspace
    ):

        return AgentContext(

            mission=mission,

            workspace=workspace
        )
