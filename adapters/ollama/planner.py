"""
Ollama Planner
"""

import json
import re

from .client import OllamaClient



class OllamaPlanner:


    def __init__(self):

        self.client = OllamaClient()



    def extract_json(
        self,
        text: str
    ):


        # Cas 1 :
        # bloc markdown ```json ... ```

        match = re.search(
            r"```json\s*(.*?)\s*```",
            text,
            re.DOTALL
        )


        if match:

            return match.group(1)



        # Cas 2 :
        # recherche du premier objet JSON

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )


        if match:

            return match.group(0)



        raise ValueError(
            "Aucun JSON trouvé dans la réponse Ollama"
        )



    def create_plan(
        self,
        goal: str
    ):


        prompt = f"""

Tu es un architecte logiciel senior.

Analyse cette demande :

{goal}


Retourne uniquement un objet JSON.

Ne mets aucun texte avant ou après.

Format :

{{
 "architecture": {{
   "backend":"",
   "database":"",
   "frontend":""
 }},

 "tasks":[
   {{
    "agent":"",
    "description":""
   }}
 ]
}}

"""


        response = self.client.chat(
            prompt
        )


        json_text = self.extract_json(
            response
        )


        return json.loads(
            json_text
        )
