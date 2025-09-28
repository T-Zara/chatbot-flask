# uncomment to test rule based chatbot
from flask import Flask, request, jsonify
import requests
url = "http://127.0.0.1:5000/chat"
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "break", "end"]:
        break
    response = requests.post(url, json={"message": user_input})
    print("Bot:", response.json()["reply"])

# End of testing of rule based chatbot code