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
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleModelChange = (e) => {
    setSelectedModel(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponseMessage("Getting your results ready...");

    try {
      const requestBody = { ...formData };

      const response = await axios.post(
        `https://be11-2607-fa49-3c43-3400-3c35-25db-dfcd-6794.ngrok-free.app/api/tabular/ai-model/${selectedModel}`,
        requestBody
      );

      let model = "";
      switch (selectedModel) {
        case "logistic":
          model = "Logistic Regression";
          break;
        case "randomforest":
          model = "Random Forest";
          break;
        case "decisiontree":
          model = "Decision Tree";
          break;
        case "svm":
          model = "Support Vector Machine";
          break;
        default:
          break;
      }

      // Add 1 second delay before showing result
      setTimeout(() => {
        setResponseMessage(
          `${model} Model Prediction: ${response.data.prediction}`
        );
        setLoading(false);
      }, 1000);
    } catch (error) {
      setTimeout(() => {
        setResponseMessage(
          `Error: ${error.response ? error.response.data.error : error.message}`
        );
        setLoading(false);
      }, 1000);
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

        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict"}
        </button>
      </form>
      {responseMessage && <p className="response">{responseMessage}</p>}
    </div>
  );
}

export default CancerForm;
