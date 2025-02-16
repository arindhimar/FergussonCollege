import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load datasets
linear_file = "St_Placement_Data_Linear.csv"
realistic_file = "Ln_Placement_Data_Realistic.csv"

df_linear = pd.read_csv(linear_file)
df_realistic = pd.read_csv(realistic_file)

# Feature Selection: Using average of ssc, hsc, and degree marks as independent variable
df_linear["avg_marks"] = (df_linear["ssc_p"] + df_linear["hsc_p"] + df_linear["degree_p"]) / 3
df_realistic["avg_marks"] = (df_realistic["ssc_p"] + df_realistic["hsc_p"] + df_realistic["degree_p"]) / 3

# Function to train regression model and predict values
def train_regression(df):
    X = df["avg_marks"].values.reshape(-1, 1)  # Independent Variable
    y = df["salary"].values  # Dependent Variable
    model = LinearRegression()
    model.fit(X, y)  # Train the model
    y_pred = model.predict(X)  # Predictions
    return X, y, y_pred

# Train models
X_linear, y_linear, y_pred_linear = train_regression(df_linear)
X_realistic, y_realistic, y_pred_realistic = train_regression(df_realistic)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1st Graph: Scatter (Linear Dataset)
axes[0, 0].scatter(X_linear, y_linear, color="blue")
axes[0, 0].set_title("Linear Dataset - Scatter Plot (Only Dots)")
axes[0, 0].set_xlabel("Average Marks (10th, 12th, Degree)")
axes[0, 0].set_ylabel("Salary (INR)")
axes[0, 0].grid()

# 2nd Graph: Scatter (Realistic Dataset)
axes[0, 1].scatter(X_realistic, y_realistic, color="blue")
axes[0, 1].set_title("Realistic Dataset - Scatter Plot (Only Dots)")
axes[0, 1].set_xlabel("Average Marks (10th, 12th, Degree)")
axes[0, 1].set_ylabel("Salary (INR)")
axes[0, 1].grid()

# 3rd Graph: Scatter + Best-Fit Line (Linear Dataset)
axes[1, 0].scatter(X_linear, y_linear, color="blue", label="Actual Data")
axes[1, 0].plot(X_linear, y_pred_linear, color="red", linewidth=2, label="Best Fit Line")
axes[1, 0].set_title("Linear Dataset - Best Fit Line")
axes[1, 0].set_xlabel("Average Marks (10th, 12th, Degree)")
axes[1, 0].set_ylabel("Salary (INR)")
axes[1, 0].legend()
axes[1, 0].grid()

# 4th Graph: Scatter + Best-Fit Line (Realistic Dataset)
axes[1, 1].scatter(X_realistic, y_realistic, color="blue", label="Actual Data")
axes[1, 1].plot(X_realistic, y_pred_realistic, color="red", linewidth=2, label="Best Fit Line")
axes[1, 1].set_title("Realistic Dataset - Best Fit Line")
axes[1, 1].set_xlabel("Average Marks (10th, 12th, Degree)")
axes[1, 1].set_ylabel("Salary (INR)")
axes[1, 1].legend()
axes[1, 1].grid()

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
