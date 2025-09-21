import logging
from flask import request
from flask.views import MethodView
from marshmallow import ValidationError

from enums.ResponseStatus import ResponseStatus
from services.CalculationService import CalculationService
from services.ValidationService import ValidationService
from util.ResponseUtil import generate_response


class CalculateView(MethodView):
	def __init__(self, logger=None):
		self.logger = logger or logging.getLogger(__name__)
		self.validation_service = ValidationService(logger)
		self.calculation_service = CalculationService(logger)

	def post(self):
		try:
			payload = request.get_json()
			self.validation_service.validate_xirr_calculation_request(payload)
			res = self.calculation_service.calculate_xirr(payload['cashflows'], payload['dates'])
			return generate_response(ResponseStatus.SUCCESS, res, 200)

		except ValidationError as e:
			self.logger.error(f"Validation Error in Xirr Calculation Request: {e.messages}")
			return generate_response(ResponseStatus.ERROR, e.messages, 400)

		except Exception as e:
			self.logger.error(f"Error Occurred while Xirr Calculation: {str(e)}")
			return generate_response(ResponseStatus.ERROR, e, 500)

