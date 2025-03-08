from flask import Flask, render_template, jsonify, request
from flask_cors import CORS  # Allows React to communicate with Flask

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    """Returns hardcoded data for testing frontend"""
    hardcoded_data = {
        "values": [5, 15, 25, 10, 30, 18, 20]  
    }
    return jsonify(hardcoded_data)

@app.route('/api/status', methods=['GET'])
def status():
    # Returns a JSON response
    return jsonify({
        "statusCode": 200,
        "status": "ok"
        })

@app.route('/api/ai-model', methods=['POST'])
def ai_model():
    try:
        data = request.json  # Get JSON data from request
        print("Received data:", data)  # Print in terminal

        # Process data (for now, just echo it back)
        response = {"message": "Data received!", "receivedData": data}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

if __name__ == '__main__':
    # Run on port 5000 by default; debug=True for auto-reload in dev
    app.run(debug=True, port=5000)