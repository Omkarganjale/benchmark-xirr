import logging
import pandas as pd
import yfinance as yf

from models import BenchmarkRecord


class FinancialDataService:
	def __init__(self, logger=None):
		self.logger = logger or logging.getLogger(__name__)

	def get_financial_data(self, ticker: str, start_date, end_date):
		try:
			self.logger.debug(f"Fetching financial data for {ticker} from {start_date} till {end_date}")
			finance_data = yf.download(ticker, group_by='ticker', start=start_date, end=end_date)
			finance_data = self.clean_data(ticker, finance_data, start_date, end_date)
			self.logger.debug(f"Found data from date {finance_data['date'].min()} till {finance_data.max()}")
			return finance_data

		except Exception as e:
			self.logger.error(f"Error occurred while fetching financial data: {str(e)}")

	@staticmethod
	def clean_data(ticker: str, data: pd.DataFrame, start_date, end_date):
		data = data.reset_index()
		if isinstance(data.columns, pd.MultiIndex):
			data.columns = [col[1] if col[1] != '' else col[0] for col in data.columns]

		result = data[['Date', 'Close']].copy()
		result['ticker'] = ticker
		result = result.rename(columns={'Close': 'close_value', 'Date': 'date'})

		result = result.reset_index()
		result['date'] = pd.to_datetime(result['date']).dt.strftime('%Y-%m-%d')
		result['ticker'] = ticker

		all_dates = pd.DataFrame({
			'date': pd.date_range(start=start_date, end=end_date).strftime('%Y-%m-%d')
		})
		result = pd.merge(all_dates, result, on='date', how='left')
		result['close_value'] = result['close_value'].ffill()
		result['ticker'] = result['ticker'].fillna(ticker)
		result = result.dropna(subset=['close_value'])
		result['id'] = result.apply(lambda row: BenchmarkRecord.generate_key(row['ticker'], row['date']), axis=1)

		return result
