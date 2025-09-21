from flask import Flask
from config import Config
from views import api_bp


def configure_app(bootstrap_app):
    bootstrap_app.config.from_object(Config)
    bootstrap_app.register_blueprint(api_bp)
    return bootstrap_app


if __name__ == '__main__':
    app = Flask(__name__)
    app = configure_app(app)
    app.run()
