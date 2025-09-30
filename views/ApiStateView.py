import logging
from flask.views import MethodView

from enums.ResponseStatus import ResponseStatus
from services.CachingService import CachingService
from util.ResponseUtil import generate_response


class ApiStateView(MethodView):
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.caching_service = CachingService(self.logger)

	def get(self):
		self.logger.info("API Cached data state requested")
		cached_ranges = self.caching_service.get_data_specs()
		return generate_response(ResponseStatus.SUCCESS, cached_ranges, 200)
