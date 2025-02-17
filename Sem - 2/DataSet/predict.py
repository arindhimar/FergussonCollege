import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset (Using Realistic Data for training)
realistic_file = "Ln_Placement_Data_Realistic.csv"
df_realistic = pd.read_csv(realistic_file)

# Feature Selection: Compute the average of SSC, HSC, and Degree marks as independent variable
df_realistic["avg_marks"] = (df_realistic["ssc_p"] + df_realistic["hsc_p"] + df_realistic["degree_p"]) / 3

# Prepare training data
X = df_realistic["avg_marks"].values.reshape(-1, 1)  # Independent Variable
y = df_realistic["salary"].values  # Dependent Variable

# Train the model
model = LinearRegression()
model.fit(X, y)  # Train the Linear Regression model

# Function to predict salary for new candidates
def predict_salary(ssc, hsc, degree):
    avg_marks = (ssc + hsc + degree) / 3  # Compute average marks
    predicted_salary = model.predict([[avg_marks]])[0]  # Predict salary
    return predicted_salary


while True:
    # Input marks of the candidate
    ssc = float(input("Enter SSC Percentage: "))
    hsc = float(input("Enter HSC Percentage: "))
    degree = float(input("Enter Degree Percentage: "))

    # Predict salary
    salary = predict_salary(ssc, hsc, degree)
    print(f"Predicted Salary: {salary:.2f} INR\n")
    
    # Ask user if they want to continue
    choice = input("Do you want to predict salary for another candidate? (yes/no): ")
    if choice.lower() != "yes":
        break