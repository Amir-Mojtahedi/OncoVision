import pickle
import numpy as np
from PIL import Image
from flask import Flask, jsonify, request
from flask_cors import CORS
from keras.api.models import load_model
from ai.utils.aiUtils import scaler, top_5

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://oncovision-front-end.onrender.com"]}}, supports_credentials=True)

cnn_model = load_model('./ai/models/cnn_model.keras')
logistic_model = pickle.load(open('./ai/models/logistic_model.sav', 'rb'))
random_forest_model = pickle.load(open('./ai/models/random_forest_model.sav', 'rb'))
svm_model = pickle.load(open('./ai/models/svm_model.sav', 'rb'))
decision_tree_model = pickle.load(open('./ai/models/decision_tree_model.sav', 'rb'))

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"statusCode": 200, "status": "ok"})

@app.route('/api/tabular/ai-model/<model_name>', methods=['POST'])
def ai_tabular_model(model_name):
    try:
        data = request.json  

        # Extract feature values in the same order as 'top_5'
        input_values = [data[feature] for feature in top_5]

        # Convert to NumPy array and scale it
        input_array = np.array(input_values).reshape(1, -1)
        input_scaled = scaler.transform(input_array)

        # Predict using the model specified in the path
        prediction = None
        match model_name.lower():
            case 'logistic':
                prediction = logistic_model.predict(input_scaled)[0]
            case 'randomforest':
                prediction = random_forest_model.predict(input_scaled)[0]
            case 'decisiontree':
                prediction = decision_tree_model.predict(input_scaled)[0]
            case 'svm':
                prediction = svm_model.predict(input_scaled)[0]
            case _:
                return jsonify({"error": f"Invalid model name: {model_name}"}), 400

        tumor = "Malignant" if prediction == 1 else "Benign"
        
        # Return the prediction
        return jsonify({"prediction": tumor}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/image/ai-model/cnn', methods=['POST'])
def ai_image_model():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        # Read the image file and convert to RGB
        image = Image.open(file.stream).convert("RGB")

        # Resize to match the model's input shape
        image = image.resize((224, 224))

        # Convert to numpy array and normalize
        image_array = np.array(image) 

        # Reshape to match the model input: (1, height, width, channels)
        image_array = image_array.reshape(1, 224, 224, 3)

        # Predict using the CNN model
        prediction = cnn_model.predict(image_array)
        tumor = "Malignant" if prediction[0][0] > 0.5 else "Benign"

        return jsonify({"prediction": tumor}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
