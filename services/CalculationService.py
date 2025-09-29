import logging
import pyxirr

from services.CachingService import CachingService


class CalculationService:

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.caching_service = CachingService(self.logger)

    def calculate_xirr(self, cashflows, dates):
        self.logger.info("Calculating XIRR")
        return pyxirr.xirr(dates, cashflows)

    def calculate_benchmark_portfolio_value(self, benchmark, dates, cashflows) -> float:
        self.logger.info(f"Calculating Benchmark Portfolio Value for {benchmark.name}")
        benchmark_values = self.caching_service.batch_get_ticker_value(benchmark.value, dates)

        units = 0
        for i in range(len(cashflows)):
            units += (-cashflows[i])/benchmark_values[i]
            self.logger.info(f"unit: {units}, cashflow: {cashflows[i]}, benchmark_value: {benchmark_values[i]}")
        res = units*benchmark_values[-1]
        self.logger.info(f"Final Benchmark Portfolio value for {benchmark.name}: {res}")
        return res
