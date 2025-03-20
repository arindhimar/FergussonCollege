import React, { useState } from "react";
import ProgressBar from "../src/components/ProgressBar";

function App() {
  const [progress, setProgress] = useState(0);

  const increaseProgress = () => {
    setProgress((prev) => (prev < 100 ? prev + 10 : 100));
  };

  const decreaseProgress = () => {
    setProgress((prev) => (prev > 0 ? prev - 10 : 0));
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Custom Progress Bar</h1>
      <ProgressBar progress={progress} height="25px" color="#007BFF" />
      <div style={{ marginTop: "20px" }}>
        <button onClick={decreaseProgress} style={buttonStyle}>Decrease</button>
        <button onClick={increaseProgress} style={buttonStyle}>Increase</button>
      </div>
    </div>
  );
}

const buttonStyle = {
  padding: "10px 20px",
  margin: "10px",
  fontSize: "16px",
  backgroundColor: "#007BFF",
  color: "#fff",
  border: "none",
  borderRadius: "5px",
  cursor: "pointer",
};

export default App;
