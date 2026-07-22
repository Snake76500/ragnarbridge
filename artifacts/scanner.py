from pathlib import Path


class ArtifactScanner:


    def scan(self, workspace):

        print("=== SCANNER DEBUG ===")
        print("WORKSPACE OBJ:", workspace)
        print("WORKSPACE PATH:", workspace.path)

        root = Path(workspace.path)

        print("EXISTS:", root.exists())
        print("FILES:")

        for f in root.rglob("*"):
            print(f)

        print("====================")


        artifacts = []


        for file in root.rglob("*"):

            if file.is_file():

                artifacts.append(
                    {
                        "name": file.name,
                        "path": str(
                            file.relative_to(root)
                        )
                    }
                )


        return artifacts
