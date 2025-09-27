import requests

url = "http://127.0.0.1:5000/chat"
payload = {"message": "Hello bot, how are you?"}

response = requests.post(url, json=payload)
print(response.json())
