import logging
import sys
import traceback

from flask import Flask

from config import Config
from views import api_bp


def configure_app(bootstrap_app):
    bootstrap_app.config.from_object(Config)

    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format=Config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(Config.LOG_FILE),
            logging.StreamHandler()
        ]
    )

    logging.getLogger('yfinance').setLevel(logging.ERROR)

    bootstrap_app.register_blueprint(api_bp)
    return bootstrap_app


if __name__ == '__main__':
    try:
        app = Flask(__name__)
        app = configure_app(app)
        logger = logging.getLogger(__name__)
        logger.info("Starting Flask application...")
        app.run(debug=True)
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to start application: {str(e)}")
        logger.error(traceback.format_exc())
        sys.exit(1)
