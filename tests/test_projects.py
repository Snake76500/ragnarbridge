from projects.manager import ProjectManager


manager = ProjectManager()


project = manager.create_project(
    "demo_ai",
    "Premier projet généré par RagnarBridge"
)


print("Projet créé:")
print(project)


print("\nProjets existants:")
print(manager.list_projects())
