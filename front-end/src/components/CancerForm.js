import { useState } from "react";
import axios from "axios";
import "./CancerForm.css"; // Import CSS for styling

function CancerForm() {
  const [formData, setFormData] = useState({
    concave_points_worst: "",
    perimeter_worst: "",
    concave_points_mean: "",
    radius_worst: "",
    perimeter_mean: "",
  });

  const [responseMessage, setResponseMessage] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/ai-model",
        formData
      );
      setResponseMessage(`Prediction: ${response.data.prediction}`);
    } catch (error) {
      setResponseMessage(
        `Error: ${error.response ? error.response.data : error.message}`
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
        <button type="submit">Predict</button>
      </form>
      {responseMessage && <p className="response">{responseMessage}</p>}
    </div>
  );
}

export default CancerForm;
