from pathlib import Path


class ArtifactReader:


    def list_files(
        self,
        workspace
    ):

        docs = (
            Path(workspace.path)
            / "docs"
        )


        if not docs.exists():

            return []


        return [
            str(file)
            for file in docs.rglob("*")
            if file.is_file()
        ]



    def read(
        self,
        workspace,
        filename
    ):

        path = (
            Path(workspace.path)
            / filename
        )

        if not path.exists():

            return None


        return path.read_text(
            encoding="utf-8"
        )
