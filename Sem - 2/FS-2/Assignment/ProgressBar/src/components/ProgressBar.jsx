import React from "react";

const ProgressBar = ({ progress, height = "20px", color = "#4caf50" }) => {
  const containerStyle = {
    width: "100%",
    backgroundColor: "#ddd",
    borderRadius: "5px",
    overflow: "hidden",
  };

  const fillerStyle = {
    width: `${progress}%`,
    height: height,
    backgroundColor: color,
    textAlign: "center",
    lineHeight: height,
    color: "white",
    fontWeight: "bold",
    transition: "width 0.3s ease-in-out",
  };

  return (
    <div style={containerStyle}>
      <div style={fillerStyle}>{progress}%</div>
    </div>
  );
};

export default ProgressBar;
