from flask import Flask, request,jsonify

app = Flask(__name__)

rules = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hey there! 👋",
    "bye": "Goodbye! Have a nice day!",
    "thanks": "You're welcome! 😊",
    "help": "Sure, I can help you. Please tell me more about your issue.",
}


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").lower()
    replay = None
    for keyword, response in rules.items():
        if keyword in user_msg:
            replay = response
            break
    if not replay:
        replay = "Cant Understand You, you weirdo"
    return jsonify({"reply": replay})    

if __name__ == "__main__":
    app.run(debug=True)
