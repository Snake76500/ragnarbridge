from .base import Agent


class BackendAgent(Agent):


    def __init__(self):

        super().__init__(
            "Backend Developer"
        )


    def execute(
        self,
        task,
        context=None
    ):

        architecture = None


        if context:

            architecture = (
                context.read_artifact(
                    "docs/architecture.md"
                )
            )


        return f"""
Backend Agent exécuté :

Tâche :
{task.description}


Architecture disponible :

{architecture or "Aucune architecture trouvée"}
"""
