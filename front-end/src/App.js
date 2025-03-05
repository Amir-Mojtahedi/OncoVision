import React, { useEffect, useState } from "react";
import axios from "axios";
import BarChart from "./BarChart";          
import PostRequest from "./components/PostRequest"; 

function App() {
  const [values, setValues] = useState([]);

  // Fetch data for the bar chart
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

  return (
    <div className="App">
      <header className="App-header">
        {/* Combined heading */}
        <h1>Data Visualization Dashboard</h1>

        {/* Existing code from develop branch */}
        <p>Welcome to OncoVision! Here is a POST request:</p>
        <PostRequest />
      </header>

      {/* Render the D3 bar chart with data from Flask */}
      <BarChart data={values} />

    </div>
  );
}

export default App;
