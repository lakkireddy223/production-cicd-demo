import os
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    app.config["APP_NAME"] = os.getenv(
        "APP_NAME",
        "Production Flask App"
    )

    @app.route("/")
    def home():
        return jsonify({
            "message": app.config["APP_NAME"]
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy"
        })

    return app
# from flask import Flask, jsonify


# def create_app():
#     app = Flask(__name__)

#     @app.route("/")
#     def home():
#         return jsonify({
#             "message": "Production Ready CI/CD Flask App is doing by Yuvansh and Janvika"
#         }), 200

#     @app.route("/health")
#     def health():
#         return jsonify({
#             "status": "healthy"
#         }), 200

#     return app
