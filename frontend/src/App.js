import React, { useEffect, useState } from "react";
import axios from "axios"; // Import Axios
import BarChart from "./BarChart";  // import your BarChart component

function App() {
  const [values, setValues] = useState([]);
  const [response, setResponse] = useState(""); // State to store API responses

  // Fetch initial data for the chart
  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/data")  
      .then((response) => {
        console.log("Data from Flask:", response.data);
        if (response.data.values) {
          setValues(response.data.values);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  // Function to handle button clicks and fetch from different routes
  const fetchData = (endpoint) => {
    axios.get(`http://127.0.0.1:5000${endpoint}`)
      .then((res) => {
        setResponse(JSON.stringify(res.data, null, 2)); // Pretty-print JSON
      })
      .catch((err) => {
        setResponse(`Error: ${err.message}`);
      });
  };

  return (
    <div className="app-container">
      <header>
        <h1>Data Visualization Dashboard</h1>
        <p>Powered by React + D3</p>
      </header>

      {/* Buttons for API Testing */}
      <div className="button-container">
        <button onClick={() => fetchData("/")}>Home</button>
        <button onClick={() => fetchData("/status")}>Status</button>
        <button onClick={() => fetchData("/api/data")}>API Data</button>
      </div>

      {/* Display API response */}
      <div className="response-container">
        <h3>Response:</h3>
        <pre>{response || "Click a button to see the response..."}</pre>
      </div>

      {/* Pass the 'values' array to your BarChart component */}
      <BarChart data={values} />

      <footer>
        &copy; OncoVision All rights reserved.
      </footer>
    </div>
  );
}

export default App;
