from flask import Blueprint

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
