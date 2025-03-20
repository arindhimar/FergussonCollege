import React, { Component } from "react";

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      email: "",
      phone: "",
      age: "",
      message: "",
      errors: {},
    };
  }

  validate = () => {
    let errors = {};
    if (this.state.name.trim().length < 3)
      errors.name = "Full Name must be at least 3 characters";
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.state.email))
      errors.email = "Invalid email address";
    if (!/^\d{10}$/.test(this.state.phone))
      errors.phone = "Phone number must be 10 digits";
    if (this.state.age < 12 || this.state.age > 100)
      errors.age = "Age must be between 12 and 100";
    if (this.state.message.trim().length < 10)
      errors.message = "Message must be at least 10 characters";

    return errors;
  };

  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    let errors = this.validate();
    if (Object.keys(errors).length > 0) {
      this.setState({ errors });
      return;
    }

    console.log("Submitted Data:", this.state);
    alert("✅ Form submitted successfully!");
    this.setState({ name: "", email: "", phone: "", age: "", message: "", errors: {} });
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit} style={styles.form}>
        <h2>Contact Form</h2>

        <input
          type="text"
          name="name"
          placeholder="Full Name"
          value={this.state.name}
          onChange={this.handleChange}
          style={styles.input}
        />
        {this.state.errors.name && <p style={styles.error}>{this.state.errors.name}</p>}

        <input
          type="email"
          name="email"
          placeholder="Email Address"
          value={this.state.email}
          onChange={this.handleChange}
          style={styles.input}
        />
        {this.state.errors.email && <p style={styles.error}>{this.state.errors.email}</p>}

        <input
          type="tel"
          name="phone"
          placeholder="Phone Number"
          value={this.state.phone}
          onChange={this.handleChange}
          style={styles.input}
        />
        {this.state.errors.phone && <p style={styles.error}>{this.state.errors.phone}</p>}

        <input
          type="number"
          name="age"
          placeholder="Age"
          value={this.state.age}
          onChange={this.handleChange}
          style={styles.input}
        />
        {this.state.errors.age && <p style={styles.error}>{this.state.errors.age}</p>}

        <textarea
          name="message"
          placeholder="Enter your message"
          value={this.state.message}
          onChange={this.handleChange}
          style={styles.textarea}
        />
        {this.state.errors.message && <p style={styles.error}>{this.state.errors.message}</p>}

        <button type="submit" style={styles.button}>Submit</button>
      </form>
    );
  }
}

const styles = {
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    maxWidth: "400px",
    margin: "auto",
    padding: "20px",
    border: "1px solid #ccc",
    borderRadius: "8px",
  },
  input: {
    padding: "10px",
    fontSize: "16px",
    borderRadius: "5px",
    border: "1px solid #aaa",
  },
  textarea: {
    padding: "10px",
    fontSize: "16px",
    borderRadius: "5px",
    border: "1px solid #aaa",
    height: "80px",
    resize: "none",
  },
  button: {
    padding: "10px",
    fontSize: "18px",
    backgroundColor: "#007BFF",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  error: {
    color: "red",
    fontSize: "14px",
    marginTop: "-8px",
  },
};

export default Form;
