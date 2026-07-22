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
         workspace=None
     ):

        self.registry = registry
        self.workspace = workspace


    def execute(self, task: object):

        
        print(
            "EXECUTOR WORKSPACE:",
            self.workspace
        )

        print(
            f"\nExecution task {task.id}"
        )

        print(
            f"Agent : {task.agent}"
        )


        task.status = TaskStatus.RUNNING


        agent = AgentFactory.create(
             task.agent,
            self.workspace
        )

        result = agent.execute(
            task,
            self.workspace
        )

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
