from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Training data
training_sentences = [
    "hi", "hello", "hey", "good morning", "good evening",
    "bye", "goodbye", "see you", "farewell",
    "how are you", "what's up", "how's it going",
    "what is the weather", "tell me the weather", "weather forecast"
]
training_labels = [
    "greeting", "greeting", "greeting", "greeting", "greeting",
    "goodbye", "goodbye", "goodbye", "goodbye",
    "smalltalk", "smalltalk", "smalltalk",
    "weather", "weather", "weather"
]

# Vectorize and train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(training_sentences)

model = MultinomialNB()
model.fit(X, training_labels)

# Responses
responses = {
    "greeting": "Hello there! 👋",
    "goodbye": "Goodbye! Have a nice day! 🌸",
    "smalltalk": "I'm just a bot, but I'm doing great!",
    "weather": "Sorry, I can’t fetch live weather yet. 🌦️"
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # Predict intent
    X_test = vectorizer.transform([user_message])
    predicted_intent = model.predict(X_test)[0]
    
    # Pick response
    reply = responses.get(predicted_intent, "Sorry, I didn't understand that.")
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
