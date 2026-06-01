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

if __name__ == "__main__":
    app.run(debug=True)