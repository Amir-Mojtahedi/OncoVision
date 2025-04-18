from flask import Flask, jsonify, request
from flask_cors import CORS  
import numpy as np
from ai.models.logisticModel import logisticRegressionModel
from ai.models.decisionTree import decisionTreeModel
from ai.models.randomforestmodel import randomForestModel
from ai.models.svm import svmModel
from ai.utils.aiUtils import scaler, top_5

app = Flask(__name__)
CORS(app)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"statusCode": 200, "status": "ok"})

@app.route('/api/ai-model', methods=['POST'])
def ai_model():
    try:
        data = request.json  

        # Extract feature values in the same order as 'top_5'
        input_values = [data[feature] for feature in top_5]

        # Convert to NumPy array and scale it
        input_array = np.array(input_values).reshape(1, -1)
        input_scaled = scaler.transform(input_array)

        # Predict using the model
        prediction = None
        match data['model']:
            case 'logistic':
                prediction = logisticRegressionModel.predict(input_scaled)[0]
            case 'randomforest':
                prediction = randomForestModel.predict(input_scaled)[0]
            case 'decisiontree':
                prediction = decisionTreeModel.predict(input_scaled)[0]
            case 'svm':
                prediction = svmModel.predict(input_scaled)[0]
            case _:
                return jsonify({"error": "Invalid model name"}), 400

        tumor = "Malignant" if prediction == 1 else "Benign"
        
        # Return the prediction
        return jsonify({"prediction": tumor}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
