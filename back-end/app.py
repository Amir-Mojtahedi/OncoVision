from flask import Flask, render_template, jsonify, request
from flask_cors import CORS  # Allows React to communicate with Flask

# Create the Flask app, pointing to the React build folder
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ---------------------------
# ROUTES FROM DEVELOP
# ---------------------------

@app.route('/api/status', methods=['GET'])
def status():
    """
    Returns a standardized status response.
    """
    return jsonify({
        "statusCode": 200,
        "status": "ok"
    })

@app.route('/api/ai-model', methods=['POST'])
def ai_model():
    try:
        data = request.json  # Get JSON data from request

        # Process data (for now, juest echo it back)
        response = {"message": "Data received!", "receivedData": data}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Run on port 5000 by default; debug=True for auto-reload in dev
    app.run(port=5000, debug=True)
