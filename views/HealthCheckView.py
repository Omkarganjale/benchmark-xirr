from flask import jsonify
from flask.views import MethodView


class HealthCheckView(MethodView):
    """API Health Check"""
    def get(self):
        return jsonify({
            'status': 'success',
            'message': 'API is running',
            'version': '1.0.0'
        }), 200
