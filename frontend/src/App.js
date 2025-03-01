import React, { useEffect, useState } from "react";
import axios from "axios"; // Import Axios
import BarChart from "./BarChart";  // import your BarChart component

function App() {
  const [values, setValues] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/data")  // Use Axios instead of fetch
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

  return (
    <div className="app-container">
      <header>
        <h1>Data Visualization Dashboard</h1>
        <p>Powered by React + D3</p>
      </header>

      {/* Pass the 'values' array to your BarChart component */}
      <BarChart data={values} />

      <footer>
        &copy; OncoVision All rights reserved.
      </footer>
    </div>
  );
}

export default App;
