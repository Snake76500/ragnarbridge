from unittest.mock import MagicMock
from adapters.ollama.planner import OllamaPlanner


def test_ollama_planner_json_extraction():
    planner = OllamaPlanner()
    raw_response = '```json\n{"tasks": [{"agent": "Dev", "description": "Test"}]}\n```'
    extracted = planner.extract_json(raw_response)
    assert '{"tasks":' in extracted

