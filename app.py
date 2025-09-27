# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask is working!"

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     user_message = data.get("message", "")
#     # For now, return a dummy reply
#     return jsonify({"reply": f"You said: {user_message}"})

# if __name__ == "__main__":
#     app.run(debug=True)


# from openai import OpenAI

# client = OpenAI(
#   api_key="Your key"
# )

# response = client.responses.create(
#   model="gpt-5-nano",
#   input="write a haiku about ai",
#   store=True,
# )

# print(response.output_text);


import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        # Call OpenAI Chat API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # you can use gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
