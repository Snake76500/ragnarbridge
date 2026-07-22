from adapters.antigravity.client import AntigravityClient


client = AntigravityClient()

response = client.generate(
    "Explique en une phrase ce que fait une API REST"
)

print(response)
