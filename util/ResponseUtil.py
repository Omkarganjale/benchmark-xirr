from datetime import datetime
from typing import Any
from flask import jsonify
from enums.ResponseStatus import ResponseStatus


def generate_response(status: ResponseStatus, value: Any, http_status: int):
	if status == ResponseStatus.SUCCESS:
		return jsonify({
			"status": ResponseStatus.SUCCESS.name,
			"value": value
		}), http_status

	else:
		return jsonify({
			"status": ResponseStatus.ERROR.name,
			"errorReferenceCode": datetime.now().strftime("%Y%m%d-%H%M%S"),
			"message": value
		}), http_status
