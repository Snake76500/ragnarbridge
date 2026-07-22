from missions.tasks import Task


task = Task(

    id=1,

    agent="Backend Developer",

    description="Créer API FastAPI"

)


print(task)

print(task.status.value)
