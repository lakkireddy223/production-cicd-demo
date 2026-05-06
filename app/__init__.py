
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({
            "message": "Production Ready CI/CD Flask App is doing by Yuvansh and Janvika"
        }), 200

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy"
        }), 200

    return app
