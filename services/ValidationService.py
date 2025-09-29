import logging
from typing import Dict, Any

from schemas.XirrCalculationRequestSchema import XirrCalculationRequestSchema


class ValidationService:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.schema = XirrCalculationRequestSchema()

    def validate_xirr_calculation_request(self, request: Dict[str, Any]):
        self.logger.info("Validating XIRR calculation request")
        self.schema.load(request)
