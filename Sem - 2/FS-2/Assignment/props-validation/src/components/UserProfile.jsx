import React from "react";
import PropTypes from "prop-types";

const UserProfile = ({ name, age, email, isVerified }) => {
  return (
    <div style={profileStyle}>
      <h2>User Profile</h2>
      <p><strong>Name:</strong> {name}</p>
      <p><strong>Age:</strong> {age}</p>
      <p><strong>Email:</strong> {email}</p>
      <p><strong>Verified User:</strong> {isVerified ? " Yes" : " No"}</p>
    </div>
  );
};

UserProfile.propTypes = {
  name: PropTypes.string.isRequired,  
  age: PropTypes.number.isRequired,   
  email: PropTypes.string,            
  isVerified: PropTypes.bool,         
};


UserProfile.defaultProps = {
  email: "Not Provided",
  isVerified: false,
};

const profileStyle = {
  border: "1px solid #ccc",
  padding: "15px",
  borderRadius: "8px",
  width: "250px",
  textAlign: "left",
};

export default UserProfile;
