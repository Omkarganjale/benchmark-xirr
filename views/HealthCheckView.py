from flask import jsonify
from flask.views import MethodView

from config import Config
from enums.ResponseStatus import ResponseStatus
from util.ResponseUtil import generate_response


class HealthCheckView(MethodView):
    def get(self):
        return generate_response(ResponseStatus.SUCCESS, f"API version {Config.API_VERSION} is running", 200)
