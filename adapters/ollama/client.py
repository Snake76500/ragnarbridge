"""
Ollama client adapter
"""

import requests


class OllamaClient:


    def __init__(
        self,
        model="gemma4:12b",
        url="http://localhost:11434"
    ):

        self.model = model
        self.url = url



    def chat(
        self,
        prompt: str
    ) -> str:


        response = requests.post(

            f"{self.url}/api/generate",

            json={

                "model": self.model,

                "prompt": prompt,

                "stream": False,

                "options": {

                    "temperature": 0.2,

                    "num_ctx": 4096

                }

            },

            timeout=900

        )


        response.raise_for_status()


        return response.json()["response"]
