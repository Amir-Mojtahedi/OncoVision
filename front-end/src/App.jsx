import CancerForm from "./components/CancerForm";
import "./App.css"; // Import the new CSS file

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to OncoVision</h1>
        <p>
          This tool helps predict breast cancer using AI. Enter the required medical 
          measurements into the form below, and our AI model will analyze the data to 
          determine if the tumor is benign or malignant.
        </p>
        <CancerForm />
      </header>
    </div>
  );
}

export default App;
