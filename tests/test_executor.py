from missions.executor import TaskExecutor
from missions.tasks import Task



task = Task(

    id=1,

    agent="Développeur Backend",

    description=
    "Créer une API FastAPI"

)



executor = TaskExecutor()



result = executor.execute(task)



print("\nRESULTAT:")
print(result)



print("\nSTATUS:")
print(result.status)



print("\nOUTPUT:")
print(result.result)
