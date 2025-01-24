from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "http://107.20.195.239"
        ]
    }
})

@app.route("/hello", methods=["GET"])
def get_hello():
    return jsonify({"Hello": "Hello"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)