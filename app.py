from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

# 1) Create the Flask app first
app = Flask(__name__, static_folder='frontend/build')

# 2) Then apply CORS to the app
CORS(app)

@app.route('/api/data')
def get_data():
    return jsonify({"values": [10, 25, 8, 15, 30, 18]})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    if path != "" and os.path.exists("frontend/build/" + path):
        return send_from_directory('frontend/build', path)
    else:
        return send_from_directory('frontend/build', 'index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=False)
