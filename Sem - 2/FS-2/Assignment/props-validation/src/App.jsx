import React from "react";
import UserProfile from "../src/components/UserProfile";

function App() {
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>PropTypes Validation Example</h1>
      <UserProfile name="Arin Dhimar" age={25} email="arin@example.com" isVerified={true} />
      <UserProfile name="Lol Npp" age={30} />
    </div>
  );
}

export default App;
