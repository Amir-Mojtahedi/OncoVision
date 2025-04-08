import { useState } from "react";
import axios from "axios";
import "./CancerForm.css";

function CancerForm() {
  const [formData, setFormData] = useState({
    concave_points_worst: "",
    perimeter_worst: "",
    concave_points_mean: "",
    radius_worst: "",
    perimeter_mean: "",
  });

  const [selectedModel, setSelectedModel] = useState("logistic");
  const [responseMessage, setResponseMessage] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleModelChange = (e) => {
    setSelectedModel(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const requestBody = {
        ...formData,
        model: selectedModel,
      };

      const response = await axios.post(
        "http://127.0.0.1:5000/api/ai-model",
        requestBody
      );
      setResponseMessage(`Prediction: ${response.data.prediction}`);
    } catch (error) {
      setResponseMessage(
        `Error: ${error.response ? error.response.data.error : error.message}`
      );
    }
  };

  return (
    <div className="form-container">
      <h2>Breast Cancer Prediction</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div key={key} className="input-group">
            <label>{key.replace(/_/g, " ")}</label>
            <input
              type="number"
              name={key}
              value={formData[key]}
              onChange={handleChange}
              required
            />
          </div>
        ))}

        <div className="model-selection">
          <p>Select AI Model:</p>
          {["logistic", "randomforest", "decisiontree", "svm"].map((model) => (
            <div key={model} className="radio-group">
              <label key={model} htmlFor={model} className="radio-label">
                {model.charAt(0).toUpperCase() + model.slice(1)}
              </label>
              <input
                type="radio"
                name="model"
                id={model}
                value={model}
                checked={selectedModel === model}
                onChange={handleModelChange}
              />
            </div>
          ))}
        </div>

        <button type="submit">Predict</button>
      </form>
      {responseMessage && <p className="response">{responseMessage}</p>}
    </div>
  );
}

export default CancerForm;
