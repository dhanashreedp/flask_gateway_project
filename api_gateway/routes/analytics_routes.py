from flask import Blueprint, request
import requests

analytics_bp = Blueprint('analytics_bp', __name__)
ANALYTICS_URL = 'http://127.0.0.1:8001'

@analytics_bp.route('/track/', methods=['GET'])
def track_event():
    response = requests.get(f"{ANALYTICS_URL}/api/track/")
    return response.json(), response.status_code
