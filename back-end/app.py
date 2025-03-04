from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os

# Create the Flask app, pointing to the React build folder
app = Flask(__name__, static_folder='frontend/build')
CORS(app)  # Enable CORS for all routes

# ---------------------------
# ROUTES FROM LUKE'S BRANCH PLEASE TELL ME IF YOU THINK THE DATA PART UNNECESSARY
# ---------------------------

@app.route('/')
def home():
    """
    Simple JSON response for the base route.
    """
    return jsonify({"message": "Welcome to the Flask backend!"})

@app.route('/api/data')
def get_data():
    """
    Example API route returning a small dataset.
    """
    return jsonify({"values": [10, 25, 8, 15, 30, 18]})

@app.route('/status', methods=['GET'])
def status_legacy():
    """
    Another status route (your branch).
    Returns a short JSON message about the Flask server state.
    """
    return jsonify({"status": "OK", "message": "Flask backend is running!"})

# Serve the React frontend build
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    """
    If the requested file exists in 'frontend/build', serve it.
    Otherwise, serve 'index.html' (the React SPA entry point).
    """
    if path != "" and os.path.exists(os.path.join("frontend/build", path)):
        return send_from_directory('frontend/build', path)
    else:
        return send_from_directory('frontend/build', 'index.html')

# ---------------------------
# ROUTES FROM DEVELOP
# ---------------------------

@app.route('/api/status', methods=['GET'])
def status_api():
    """
    JSON status route (develop branch).
    Returns a standardized status response.
    """
    return jsonify({
        "statusCode": 200,
        "status": "ok"
    })

@app.route('/api/ai-model', methods=['POST'])
def ai_model():
    """
    Example POST endpoint. Logs and echoes back the received JSON data.
    """
    try:
        data = request.json  # JSON body from client
        print("Received data:", data)  # Log to terminal

        # Process data here if needed
        response = {"message": "Data received!", "receivedData": data}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ---------------------------
# APP ENTRY POINT
# ---------------------------
if __name__ == '__main__':
    # Feel free to change debug to False if you prefer
    app.run(port=5000, debug=True)
