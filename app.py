from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask on Heroku!", 200

@app.route("/health")
def health():
    return jsonify(status="OK"), 200

if __name__ == "__main__":
    # bind to all interfaces so Gunicorn can route traffic correctly
    app.run(host="0.0.0.0")

