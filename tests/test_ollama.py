from adapters.ollama.client import OllamaClient


def test_ollama_client_init():
    client = OllamaClient()
    assert client.model == "gemma4:12b"
    assert client.url == "http://localhost:11434"

