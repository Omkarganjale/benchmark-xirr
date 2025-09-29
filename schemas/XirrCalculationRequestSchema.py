from datetime import date
from marshmallow import Schema, fields, validate, validates_schema, ValidationError
from config import Config
from enums.BenchmarkTicker import BenchmarkTicker


class XirrCalculationRequestSchema(Schema):
	dates = fields.List(
		fields.Date(Config.DATE_FORMAT),
		required=True,
		validate=[
			validate.Length(min=2)
		])

	cashflows = fields.List(
		fields.Float(),
		required=True,
		validate=[
			validate.Length(min=2)
		])

	benchmarks = fields.List(
		fields.Str(),
		missing=list,
		validate=[
			validate.ContainsOnly([ticker.name for ticker in BenchmarkTicker])
		]
	)

	@validates_schema
	def validates_dates_cashflow_length(self, data, **kwargs):
		cashflows_length = len(data['cashflows'])
		dates_length = len(data['dates'])
		if cashflows_length != dates_length:
			raise ValidationError('Cashflows and dates must have the same length')

		if data['cashflows'][-1] < 0:
			raise ValidationError('Last Cashflow must be current portfolio value hence non negative')

		if len(data['benchmarks']) > 0 and any(dt >= date.today() for dt in data['dates']):
			raise ValidationError('For benchmark calculation, all dates must be in past')

		if all(x > 0 for x in data['cashflows']) or all(x < 0 for x in data['cashflows']):
			raise ValidationError('All cashflows of the same sign. Atleast one positive and negative required')

		if not self.is_sorted_and_unequal(data['dates']):
			raise ValidationError('Dates must be sorted and unequal')

	@staticmethod
	def is_sorted_and_unequal(dates):
		return all(dates[i] <= dates[i+1] and dates[i] != dates[i+1] for i in range(len(dates)-1))
