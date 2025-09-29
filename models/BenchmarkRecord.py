from sqlalchemy import String, Column

from config import Config
from models.BaseModel import BaseModel


class BenchmarkRecord(BaseModel):
	__tablename__ = Config.BENCHMARK_RECORD_TABLE

	id = Column(String, primary_key=True)
	ticker = Column(String, nullable=False)
	date = Column(String, nullable=False)
	close_value = Column(String, nullable=False)

	@staticmethod
	def generate_key(ticker: str, date: str) -> str:
		return f"{ticker}#{date}"

	@staticmethod
	def __repr__(self):
		return f"<BenchmarkRecord(benchmark='{self.ticker}', date='{self.date}', value={self.close_value})>"