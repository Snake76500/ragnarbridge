from missions.planner import MissionPlanner



plan = {

    "architecture": {

        "backend": "FastAPI",

        "database": "PostgreSQL"

    },


    "tasks": [

        {

            "agent": "Database Architect",

            "description":
            "Créer le schéma PostgreSQL"

        },


        {

            "agent": "Backend Developer",

            "description":
            "Créer les endpoints REST"

        },


        {

            "agent": "QA",

            "description":
            "Créer les tests"

        }

    ]

}



planner = MissionPlanner()


tasks = planner.create_tasks(
    plan
)


for task in tasks:

    print(task)
