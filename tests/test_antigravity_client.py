from adapters.antigravity.client import AntigravityClient


def test_antigravity_client_defaults():
    client = AntigravityClient()
    assert client.timeout == 600

