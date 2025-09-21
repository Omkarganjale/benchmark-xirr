import logging
import pyxirr


class CalculationService:

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def calculate_xirr(self, cashflows, dates):
        self.logger.info("Calculating XIRR")
        return pyxirr.xirr(dates, cashflows)
