from flask import Flask, request, jsonify;

app = Flask(__name__)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    return jsonify({"replay": f"You Said: {user_msg}"})

if __name__ == "__main__":
    app.run(debug=True)