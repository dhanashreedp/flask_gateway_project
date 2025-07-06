from flask import Blueprint, request
import requests

data_bp = Blueprint('data_bp', __name__)
DATA_SERVICE_URL = 'http://127.0.0.1:8002'

@data_bp.route('/process/', methods=['POST'])
def process_text():
    data = request.get_json()
    response = requests.post(f"{DATA_SERVICE_URL}/api/process/", json=data)
    return response.json(), response.status_code
