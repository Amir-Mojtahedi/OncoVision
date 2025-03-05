import React from "./components/PostRequest";
import axios from "axios"; // Import Axios
import BarChart from "./BarChart";  // import BarChart component
function App() {

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to OncoVision! Here is a POST request
          <PostRequest />
        </p>
      </header>
    </div>
  );
}

export default App;
