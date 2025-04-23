import { useState } from "react";
import axios from "axios";
import "./ImageUpload.css";

function ImageUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [responseMessage, setResponseMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedFile) {
      setResponseMessage("Please select a PNG image.");
      return;
    }

    setLoading(true);
    setResponseMessage("Getting your results ready...");

    const formData = new FormData();
    formData.append("image", selectedFile);

    try {
      const response = await axios.post(
        "https://oncovision.onrender.com/api/image/ai-model/cnn",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      setTimeout(() => {
        setResponseMessage(`Prediction: ${response.data.prediction}`);
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
    <div className="image-upload-container">
      <h2>Image-Based Breast Cancer Prediction</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="image/png"
          onChange={handleFileChange}
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Upload and Predict"}
        </button>
      </form>
      {responseMessage && <p className="response">{responseMessage}</p>}
    </div>
  );
}

export default ImageUpload;
