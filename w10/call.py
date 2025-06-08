import ollama

client = ollama.Client()

response = client.generate(model="llama2", prompt="Say hi")
print(response['response'])
