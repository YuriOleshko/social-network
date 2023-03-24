from flask import Flask


def create_app():
    app = Flask(__name__)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app


app = create_app()
from . import routes
