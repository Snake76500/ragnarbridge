"""
Antigravity Client

Wrapper autour du CLI agy
"""

from dataclasses import dataclass

import subprocess

from typing import Optional



@dataclass
class AntigravityResult:

    success: bool

    output: str

    error: Optional[str] = None

    returncode: int = 0




class AntigravityClient:


    def __init__(
        self,
        model="gemini-3.1-pro-high",
        timeout=600,
        workspace=None
    ):

        self.model = model
        self.timeout = timeout

    def generate(
        self,
        prompt: str,
        workspace=None

    ) -> AntigravityResult:

        working_directory = None

        if workspace:

            if hasattr(workspace, "path"):

                working_directory = str(
                    workspace.path
                )

            else:

                working_directory = str(
                    workspace
                )

        workspace_path = None

        if workspace:

            workspace_path = (
                workspace.path
                if hasattr(workspace, "path")
                else workspace
            )

            prompt = f"""
            Tu travailles dans le workspace suivant :

            {workspace_path}

            Toutes les créations de fichiers doivent être réalisées dans ce répertoire.

            Mission :
            {prompt}
            """


        command = [
            "agy",
            "--model",
            self.model,
            "--print",
            prompt
        ]

        try:

            print(
                "WORKSPACE:",
                working_directory
            )

            result = subprocess.run(

                command,

                cwd=working_directory,

                capture_output=True,

                text=True,

                timeout=self.timeout

                )

            print("=== AGY DEBUG ===")
            print("RETURN CODE:", result.returncode)
            print("STDOUT:")
            print(result.stdout)
            print("STDERR:")
            print(result.stderr)
            print("=================")


            if result.returncode != 0:

                return AntigravityResult(

                    success=False,

                    output="",

                    error=result.stderr,

                    returncode=result.returncode

                )


            return AntigravityResult(

                success=True,

                output=result.stdout,

                returncode=0

            )


        except subprocess.TimeoutExpired:

            return AntigravityResult(

                success=False,

                output="",

                error="Timeout"

            )


        except Exception as exc:

            return AntigravityResult(

                success=False,

                output="",
                error=str(exc)

            )
