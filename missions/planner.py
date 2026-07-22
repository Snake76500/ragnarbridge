"""
Mission planner

Convertit un plan Ollama en tâches RagnarBridge
"""

from .tasks import Task



class MissionPlanner:


    def create_tasks(
        self,
        plan: dict
    ) -> list[Task]:


        tasks = []


        for index, item in enumerate(
            plan.get("tasks", []),
            start=1
        ):

            task = Task(

                id=index,

                agent=item.get(
                    "agent",
                    "Unknown"
                ),

                description=item.get(
                    "description",
                    ""
                )

            )

            tasks.append(task)


        return tasks
