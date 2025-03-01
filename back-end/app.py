from flask import Flask, render_template, jsonify, request
from flask_cors import CORS  # Allows React to communicate with Flask

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    # Renders the templates/index.html file
    return render_template('index.html')

@app.route('/api/greeting', methods=['GET'])
def greeting():
    # Returns a JSON response
    return jsonify({"message": "Hello from Flask backend!"})

@app.route('/post-data', methods=['POST'])
def receive_data():
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
