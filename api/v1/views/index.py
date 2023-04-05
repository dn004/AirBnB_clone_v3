#!/usr/bin/python3
"""
comment
"""
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """
    returns "status": "OK"
    """
    return jsonify({"status": "OK"})

