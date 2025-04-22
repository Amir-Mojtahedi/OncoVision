import { useState } from "react";
import CancerForm from "./components/CancerForm";
import ImageUpload from "./components/ImageUpload";
import "./App.css";

function App() {
  const [activeView, setActiveView] = useState("form");

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to OncoVision</h1>
        <p>
          This tool helps predict breast cancer using AI. Choose to enter
          medical measurements manually or upload a histopathological image for
          analysis.
        </p>

        <div className="toggle-buttons">
          <button
            className={activeView === "form" ? "active-toggle" : ""}
            onClick={() => setActiveView("form")}
          >
            Tabular Input
          </button>
          <button
            className={activeView === "image" ? "active-toggle" : ""}
            onClick={() => setActiveView("image")}
          >
            Image Upload
          </button>
        </div>

        {activeView === "form" ? <CancerForm /> : <ImageUpload />}
      </header>
    </div>
  );
}

export default App;
