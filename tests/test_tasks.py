from missions.tasks import Task, TaskStatus


def test_task_creation():
    task = Task(
        id=1,
        agent="Backend Developer",
        description="Créer API FastAPI"
    )

    assert task.id == 1
    assert task.status == TaskStatus.PENDING
    assert task.status.value == "PENDING"

