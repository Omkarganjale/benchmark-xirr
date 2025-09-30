from flask import Blueprint

from views.ApiStateView import ApiStateView
from views.CalculateView import CalculateView
from views.HealthCheckView import HealthCheckView

api_bp = Blueprint('api', __name__, url_prefix='/api')

"""
	Calculate the XIRR for given dates and cashflow
	POST - /api/calculate
"""
api_bp.add_url_rule('/calculate', view_func=CalculateView.as_view('calculate'))

"""
	Health Check
	GET - /api/health
"""
api_bp.add_url_rule('/health', view_func=HealthCheckView.as_view('health_check'))

"""
	API Cached Data Specs: returns supported Benchmark Ticker & cached ranges of Benchmark
	GET - /api/state
"""
api_bp.add_url_rule('/state', view_func=ApiStateView.as_view('api_state'))

