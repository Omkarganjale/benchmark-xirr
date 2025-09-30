from sqlalchemy import Column, String

from config import Config
from models.BaseModel import BaseModel


class CacheRange(BaseModel):
	__tablename__ = Config.CACHE_RANGE_TABLE

	ticker = Column(String, primary_key=True, nullable=False)
	min_date = Column(String, nullable=False)
	max_date = Column(String, nullable=False)

	def __init__(self, ticker: str, min_date: str, max_date: str):
		self.ticker = ticker
		self.min_date = min_date
		self.max_date = max_date

	def __str__(self):
		return f"<CacheRange(ticker='{self.ticker}', min_date='{self.min_date}', max_date='{self.max_date}')>"

	def serialize(self):
		return {
			'ticker': self.ticker,
			'min_date': self.min_date,
			'max_date': self.max_date
		}