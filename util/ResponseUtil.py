from typing import Any
from flask import jsonify
from enums.ResponseStatus import ResponseStatus


def generate_response(status: ResponseStatus, value: Any, http_status: int):
	return jsonify({
		"status": str(status),
		"value": value
	}), http_status
