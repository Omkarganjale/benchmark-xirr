import logging
import pyxirr

from services.CachingService import CachingService


class CalculationService:

	def __init__(self, logger=None):
		self.logger = logger or logging.getLogger(__name__)
		self.caching_service = CachingService(self.logger)

	def calculate_xirr(self, cashflows, dates):
		try:
			self.logger.info("Calculating XIRR")
			return pyxirr.xirr(dates, cashflows)

		except (ValueError, ZeroDivisionError) as e:
			self.logger.error(f"XIRR calculation failed: {str(e)}")
			raise ValueError(f"Invalid input for XIRR calculation: {str(e)}")

		except Exception as e:
			self.logger.exception("Unexpected error in XIRR calculation")
			raise Exception(f"XIRR calculation failed: {str(e)}")

	def calculate_benchmark_portfolio_value(self, benchmark, dates, cashflows) -> float:
		try:
			self.logger.info(f"Calculating Benchmark Portfolio Value for {benchmark.name}")
			benchmark_values = self.caching_service.batch_get_ticker_value(benchmark.value, dates)

			units = 0
			self.logger.info(
				f"len of cashflows: {len(cashflows)} & len of benchmark_values: {len(benchmark_values)} & len of dates: {len(dates)}")
			for i in range(len(cashflows)):
				units += (-cashflows[i]) / benchmark_values[i]
				self.logger.info(f"unit: {units}, cashflow: {cashflows[i]}, benchmark_value: {benchmark_values[i]}")
			res = units * benchmark_values[len(dates) - 1]
			self.logger.info(f"Final Benchmark Portfolio value for {benchmark.name}: {res}")
			return res

		except ValueError as e:
			self.logger.error(f"Benchmark calculation failed: {str(e)}")
			raise ValueError(f"Benchmark calculation error: {str(e)}")
		except Exception as e:
			self.logger.exception("Unexpected error in benchmark portfolio calculation")
			raise Exception(f"Benchmark portfolio calculation failed: {str(e)}")
