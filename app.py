from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the templates/index.html file
    return render_template('index.html')

@app.route('/api/greeting', methods=['GET'])
def greeting():
    # Returns a JSON response
    return jsonify({"message": "Hello from Flask backend!"})

if __name__ == '__main__':
    # Run on port 5000 by default; debug=True for auto-reload in dev
    app.run(debug=True, port=5000)
