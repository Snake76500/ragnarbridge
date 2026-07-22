"""
Task Executor

Exécute les tâches d'une mission
"""

from .tasks import TaskStatus
from agents.registry import AgentRegistry
from agents.factory import AgentFactory


class TaskExecutor:


    def __init__(
         self,
         registry: AgentRegistry,
         context=None
     ):

        self.registry = registry
        self.context = context

    def execute(self, task: object):

        
        print(
            f"\nExecution task {task.id}"
        )

        print(
            f"Agent : {task.agent}"
        )


        task.status = TaskStatus.RUNNING


        agent = self.registry.get(
            task.agent
        )

        if agent is None:

            result = (
                f"Aucun agent trouvé pour {task.agent}"
            )

        else:

            result = agent.execute(
                task,
                self.context
            )

            if self.context and hasattr(self.context, "scan_artifacts"):
                self.context.scan_artifacts()


        task.result = result


        task.status = TaskStatus.DONE


        return task




    #
    # Agents temporaires
    # seront remplacés par MCP
    #


    def execute_architect(self, task):

        return (
            "Architecture analysée "
            "par l'architecte logiciel"
        )



    def execute_backend(self, task):

        return (
            "Code backend généré "
            "par le développeur backend"
        )



    def execute_frontend(self, task):

        return (
            "Interface frontend préparée"
        )



    def execute_security(self, task):

        return (
            "Analyse sécurité terminée"
        )



    def execute_qa(self, task):

        return (
            "Tests définis"
        )



    def execute_devops(self, task):

        return (
            "Pipeline CI/CD préparée"
        )



    def execute_default(self, task):

        return (
            "Aucun agent associé"
        )
