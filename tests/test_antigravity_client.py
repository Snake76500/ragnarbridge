from adapters.antigravity.client import AntigravityClient

client = AntigravityClient()

result = client.generate(
    "Crée une fonction Python hello_world()"
)

print(result.success)

print(result.returncode)

print(result.error)

print(result.output)
