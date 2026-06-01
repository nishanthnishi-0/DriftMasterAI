from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from chatbot.drift_engine import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    response = get_response(message)

    return jsonify({
        "response": response
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
