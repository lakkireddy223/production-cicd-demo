import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["APP_NAME"] = os.getenv(
        "APP_NAME",
        "Production Flask App"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///local.db"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

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

    @app.route("/db-check")
    def db_check():
        try:
            db.session.execute("SELECT 1")

            return jsonify({
                "database": "connected"
            })

        except Exception as e:
            return jsonify({
                "database": "failed",
                "error": str(e)
            }), 500

    with app.app_context():
        db.create_all()

    return app
# import os
# from flask import Flask, jsonify


# def create_app():
#     app = Flask(__name__)

#     app.config["APP_NAME"] = os.getenv(
#         "APP_NAME",
#         "Production Flask App"
#     )

#     @app.route("/")
#     def home():
#         return jsonify({
#             "message": app.config["APP_NAME"]
#         })

#     @app.route("/health")
#     def health():
#         return jsonify({
#             "status": "healthy"
#         })

#     return app
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
