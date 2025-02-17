import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
file_path = "High_R2_Breast_Cancer_Probability.csv"  # Ensure this file exists
df = pd.read_csv(file_path)

# Feature Selection: Tumor Size (X) and Probability of Cancer (y)
X = df["Tumor Size"].values.reshape(-1, 1)  # Independent Variable
y = df["Probability of Cancer"].values  # Dependent Variable

# Train Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Get Regression Formula
m = model.coef_[0]  # Slope
c = model.intercept_  # Intercept
print(f"Regression Equation: Probability of Cancer = {m:.4f} * Tumor Size + {c:.4f}")

# Predict values using the model
y_pred = model.predict(X)

# Calculate R² Score
r2 = r2_score(y, y_pred)
print(f"R² Value: {r2:.4f}")

# Plot Scatter and Best Fit Line
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color="blue", label="Actual Data")  # Scatter plot
plt.plot(X, y_pred, color="red", linewidth=2, label="Best Fit Line")  # Regression Line
plt.xlabel("Tumor Size (mm)")
plt.ylabel("Probability of Cancer")
plt.title("Tumor Size vs Probability of Cancer with Best Fit Line")
plt.legend()
plt.grid()
plt.show()
