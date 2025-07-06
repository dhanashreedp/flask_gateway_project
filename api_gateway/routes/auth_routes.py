from flask import Blueprint, request
import requests

auth_bp = Blueprint('auth_bp', __name__)
AUTH_SERVICE_URL = 'http://127.0.0.1:8000'

@auth_bp.route('/register/', methods=['POST'])
def register():
    data = request.get_json()
    response = requests.post(f"{AUTH_SERVICE_URL}/api/register/", json=data)
    return response.json(), response.status_code
