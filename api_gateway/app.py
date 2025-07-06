from flask import Flask, request, jsonify, make_response
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all origins, or specify origins if needed

# --- Microservice URLs ---
# Your Django Authentication Service (auth_service project)
DJANGO_AUTH_SERVICE_URL = "http://localhost:8000"

# Your Django Analytics Service (analytics_service project)
# IMPORTANT: Replace 8001 with the actual port your analytics_service is running on!
DJANGO_ANALYTICS_SERVICE_URL = "http://localhost:8001"

# Your Django Data Processing Service (data_service project)
# IMPORTANT: Replace 8002 with the actual port your data_service is running on!
DJANGO_DATA_PROCESSING_SERVICE_URL = "http://localhost:8002"


@app.route('/')
def index():
    """A simple index route for the gateway."""
    return "Welcome to the API Gateway!"

# --- Authentication Service Routes ---
@app.route('/api/auth/register/', methods=['POST'])
def register_user():
    """Proxies registration requests to the Django auth service."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        # Forward the request to the Django backend's register endpoint
        django_response = requests.post(
            f"{DJANGO_AUTH_SERVICE_URL}/api/register/",
            json={"username": username, "password": password}
        )
        response = make_response(django_response.content, django_response.status_code)
        response.headers['Content-Type'] = django_response.headers['Content-Type']
        return response

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Could not connect to the authentication service."}), 503
    except requests.exceptions.Timeout:
        return jsonify({"error": "Authentication service timed out."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with authentication service: {e}"}), 500

@app.route('/api/auth/login/', methods=['POST'])
def login_user():
    """Proxies login requests to the Django auth service."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        # Forward the request to the Django backend's login endpoint
        django_response = requests.post(
            f"{DJANGO_AUTH_SERVICE_URL}/api/login/",
            json={"username": username, "password": password}
        )
        response = make_response(django_response.content, django_response.status_code)
        response.headers['Content-Type'] = django_response.headers['Content-Type']
        return response

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Could not connect to the authentication service."}), 503
    except requests.exceptions.Timeout:
        return jsonify({"error": "Authentication service timed out."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with authentication service: {e}"}), 500

# --- Analytics Service Route ---
@app.route('/api/analytics/track/', methods=['GET'])
def track_event():
    """Proxies analytics tracking requests to the analytics service."""
    try:
        analytics_response = requests.get(
            f"{DJANGO_ANALYTICS_SERVICE_URL}/api/track/" # Corrected path for analytics_service
        )
        response = make_response(analytics_response.content, analytics_response.status_code)
        response.headers['Content-Type'] = analytics_response.headers['Content-Type']
        return response

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Could not connect to the analytics service. Is it running?"}), 503
    except requests.exceptions.Timeout:
        return jsonify({"error": "Analytics service timed out."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with analytics service: {e}"}), 500

# --- Data Processing Service Route ---
@app.route('/api/data/process/', methods=['POST'])
def process_data():
    """Proxies data processing requests to the data processing service."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    text_to_process = data.get("text")

    if not text_to_process:
        return jsonify({"error": "Text to process is required"}), 400

    try:
        data_processing_response = requests.post(
            f"{DJANGO_DATA_PROCESSING_SERVICE_URL}/api/process/", # Corrected path for data_service
            json={"text": text_to_process}
        )
        response = make_response(data_processing_response.content, data_processing_response.status_code)
        response.headers['Content-Type'] = data_processing_response.headers['Content-Type']
        return response

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Could not connect to the data processing service. Is it running?"}), 503
    except requests.exceptions.Timeout:
        return jsonify({"error": "Data processing service timed out."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with data processing service: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000) 
