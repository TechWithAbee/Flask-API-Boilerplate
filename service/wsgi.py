import os
import json
import logging.config
from werkzeug.exceptions import HTTPException
from flask_jwt_extended import JWTManager
import structlog
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify
from flask import Response
from flask_cors import CORS
from prometheus_client import CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry
from prometheus_client import generate_latest
from prometheus_client import multiprocess
from config.logger import (
    prepare_logging_config
)
from service.constants import (
    APP_LOG_LEVEL_ENV_KEY,
    SERVER_LOG_LEVEL_ENV_KEY,
    API_ERROR_UNHANDELED,
)
from helper.api_types import create_error_return
from handler.user import user_routes

def setup_logging():
    """
      Setup logging with struct log
      :return:
      """
    log_level = os.getenv(APP_LOG_LEVEL_ENV_KEY)
    logging.config.dictConfig(
        prepare_logging_config(
            int(log_level) if log_level is not None else logging.INFO
        )
    )

def init_app(use_log_handlers="gunicorn.error") -> Flask:
    """
      Init application
      :returns Flask
      """
    server_log_level = os.getenv(SERVER_LOG_LEVEL_ENV_KEY)
    flask_app = Flask(__name__)
    requested_logger = logging.getLogger(use_log_handlers)
    flask_app.logger.handlers = requested_logger.handlers[:]
    werkzeug_logger = logging.getLogger("werkzeug")
    werkzeug_logger.setLevel(
        int(server_log_level) if server_log_level is not None else logging.ERROR
    )
    log = structlog.get_logger()

    log.info(
        "the flask application was initialized",
        server_log_level=werkzeug_logger.level,
        app_log_level=logging.root.level,
    )

    return flask_app

load_dotenv(find_dotenv())

setup_logging()
app = init_app()
cors = CORS(app)

@app.errorhandler(HTTPException)
def handle_bad_request(error: Exception) -> Response:
    log = structlog.get_logger()
    log.error(error)
    return Response(
        response=json.dumps(
            create_error_return(
                API_ERROR_UNHANDELED,
                "there was unknown error. please get in touch with the support",
            )
        ),
        status=400,
        mimetype="application/json",
    )

@app.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)


app.register_blueprint(user_routes.user_bp)
app.register_error_handler(400, handle_bad_request)
