from adapters.antigravity.client import AntigravityClient


def test_antigravity_client_init():
    client = AntigravityClient()
    assert client.model == "gemini-3.1-pro-high"

