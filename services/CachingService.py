import logging

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import sessionmaker

from config import Config
from models.BaseModel import BaseModel
from models.BenchmarkRecord import BenchmarkRecord
from models.CacheRange import CacheRange
from services.FinancialDataService import FinancialDataService


class CachingService:
	def __init__(self, logger=None):
		self.logger = logger or logging.getLogger(__name__)
		self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
		self.Session = sessionmaker(bind=self.engine)
		self.data_service = FinancialDataService(logger)
		self._init_db()

	def _init_db(self):
		try:
			BaseModel.metadata.create_all(self.engine)
			self.logger.info("Database tables created/validated")
		except Exception as e:
			self.logger.error(f"Error initializing database: {str(e)}")
			raise

	def batch_get_ticker_value(self, benchmark: str, dates: list[str]):

		session = self.Session()
		try:
			self.logger.debug(f"Attempting to load cached values for {benchmark}")
			query = f""" 
			SELECT date, close_value 
			FROM {Config.BENCHMARK_RECORD_TABLE} 
			WHERE ticker = '{benchmark}' 
			ORDER BY date
			"""

			df = pd.read_sql_query(query, self.engine)
			df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

			cache_range = session.query(CacheRange).filter_by(ticker=benchmark).first()
			self.logger.debug(f"Cache range for {benchmark}: {cache_range}")

			is_cache_miss = (
				not cache_range or
				dates[0] < cache_range.min_date or
				dates[-1] > cache_range.max_date
			)

			if is_cache_miss:
				self.logger.debug(f"Cache miss for {benchmark}")

				self.logger.debug(f"Fetching from yfinance for {benchmark}")
				fetched_df = self.data_service.get_financial_data(
					benchmark,
					dates[0],
					dates[-1]
				)

				if not fetched_df.empty:
					self.logger.debug(f"Cleaning fetched data ...")
					self.logger.debug(f"Fetched data sample: {fetched_df.head()}")
					fetched_df = fetched_df.reset_index()
					fetched_df['date'] = pd.to_datetime(fetched_df['date']).dt.strftime('%Y-%m-%d')
					fetched_df['ticker'] = benchmark

					all_dates = pd.DataFrame({
						'date': pd.date_range(start=dates[0], end=dates[-1]).strftime('%Y-%m-%d')
					})
					fetched_df = pd.merge(all_dates, fetched_df, on='date', how='left')
					fetched_df['close_value'] = fetched_df['close_value'].ffill()
					fetched_df['ticker'] = fetched_df['ticker'].fillna(benchmark)
					fetched_df = fetched_df.dropna(subset=['close_value'])
					fetched_df['id'] = fetched_df.apply(lambda row: BenchmarkRecord.generate_key(row['ticker'], row['date']), axis=1)

					min_date = fetched_df['date'].min()
					max_date = fetched_df['date'].max()

					if not cache_range:
						cache_range = CacheRange(
							ticker=benchmark,
							min_date=min_date,
							max_date=max_date
						)
					else:
						cache_range.min_date = min(cache_range.min_date, min_date)
						cache_range.max_date = max(cache_range.max_date, max_date)
					self.logger.debug(f"Updated cache range for {benchmark}: {cache_range}")
					session.add(cache_range)

					self.logger.debug(f"Saving fetched data to database ...")
					# self.logger.debug(fetched_df.to_string())
					# fetched_df[['id', 'ticker', 'date', 'close_value']].to_sql(
					# 	Config.BENCHMARK_RECORD_TABLE,
					# 	self.engine,
					# 	if_exists='append',
					# 	index=False,
					# 	method='multi',
					# 	chunksize=1000
					# )

					# Convert to list of dictionaries for SQLAlchemy
					records_to_upsert = [
						{
							'id': row['id'],
							'ticker': row['ticker'],
							'date': row['date'],
							'close_value': row['close_value']
						}
						for _, row in fetched_df.iterrows()
					]

					# Use merge to handle updates/inserts
					for record in records_to_upsert:
						stmt = insert(BenchmarkRecord).values(record)
						stmt = stmt.on_conflict_do_update(
							index_elements=['id'],
							set_={
								'close_value': stmt.excluded.close_value,
								'date': stmt.excluded.date
							}
						)
						session.execute(stmt)
					session.commit()
					self.logger.debug("Successfully saved fetched data to database")

			self.logger.debug(f"Fetching from database latest values for {benchmark}")

			ids = [f"{benchmark}#{date}" for date in dates]

			records = session.query(BenchmarkRecord).filter(BenchmarkRecord.id.in_(ids)).order_by(BenchmarkRecord.date).all()
			return [float(record.close_value) for record in records]

		except Exception as e:
			self.logger.error(f"Error in batch_get_ticker_value: {str(e)}")
			session.rollback()
			raise e
		finally:
			session.close()
