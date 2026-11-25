from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Enterprise DevSecOps Platform",
        "status": "success"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/info", methods=["GET"])
def info():
    return jsonify({
        "application": "Enterprise DevSecOps Platform",
        "version": "1.0.0",
        "framework": "Flask"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
