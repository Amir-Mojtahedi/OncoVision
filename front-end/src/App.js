<<<<<<< HEAD
import React, { useEffect, useState } from "react";
import axios from "axios";
import BarChart from "./BarChart";          
import PostRequest from "./components/PostRequest"; 
=======
import CancerForm from "./components/CancerForm";
import "./App.css"; // Import the new CSS file
>>>>>>> 6164b3944c54b56dbd0ad5b1d1e88142cee5764c

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
<<<<<<< HEAD
        {/* Combined heading */}
        <h1>Data Visualization Dashboard</h1>

        {/* Existing code from develop branch */}
        <p>Welcome to OncoVision! Here is a POST request:</p>
        <PostRequest />
=======
        <h1>Welcome to OncoVision</h1>
        <p>
          This tool helps predict breast cancer using AI. Enter the required medical 
          measurements into the form below, and our AI model will analyze the data to 
          determine if the tumor is benign or malignant.
        </p>
        <CancerForm />
>>>>>>> 6164b3944c54b56dbd0ad5b1d1e88142cee5764c
      </header>

      {/* Render the D3 bar chart with data from Flask */}
      <BarChart data={values} />

    </div>
  );
}

export default App;
