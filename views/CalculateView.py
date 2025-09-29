import logging
from flask import request
from flask.views import MethodView
from marshmallow import ValidationError

from enums.BenchmarkTicker import BenchmarkTicker
from enums.ResponseStatus import ResponseStatus
from services.CalculationService import CalculationService
from services.FinancialDataService import FinancialDataService
from services.ValidationService import ValidationService
from util.ResponseUtil import generate_response


class CalculateView(MethodView):
	def __init__(self, logger=None):
		self.logger = logger or logging.getLogger(__name__)
		self.validator = ValidationService(logger)
		self.calculator = CalculationService(logger)
		self.data_service = FinancialDataService(logger)

	def post(self):
		try:
			payload = request.get_json()
			self.validator.validate_xirr_calculation_request(payload)

			xirr = {'portfolio': self.calculator.calculate_xirr(payload['cashflows'], payload['dates'])}
			for benchmark in payload['benchmarks']:
				benchmark_portfolio_value = self.calculator.calculate_benchmark_portfolio_value(
					BenchmarkTicker[benchmark],
					payload['dates'],
					payload['cashflows'][:-1])

				xirr[benchmark] = self.calculator.calculate_xirr(
					payload['cashflows'][:-1] + [benchmark_portfolio_value],
					payload['dates'])

			return generate_response(ResponseStatus.SUCCESS, xirr, 200)

		except ValidationError as e:
			self.logger.error(f"Validation Error in Xirr Calculation Request: {e.messages}")
			return generate_response(ResponseStatus.ERROR, e.messages, 400)

		except Exception as e:
			self.logger.error(f"Error Occurred while Xirr Calculation: {str(e)}")
			return generate_response(ResponseStatus.ERROR, e, 500)

