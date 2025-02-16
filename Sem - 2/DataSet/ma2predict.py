import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
file_path = "pizza_dataset2.csv"  # Change this to your actual file
df = pd.read_csv(file_path)

# Display first few rows
print(df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Encode categorical variables (Crust Type, Toppings)
encoder = LabelEncoder()
df['Topping'] = encoder.fit_transform(df['Topping'])
df['BreadType'] = encoder.fit_transform(df['BreadType'])
df['Extra Topping'] = df['Extra Topping'].astype(int)  # Convert Boolean to 0/1
df['Extra Cheese'] = df['Extra Cheese'].astype(int)    # Convert Boolean to 0/1

# Define independent (X) and dependent (y) variables
X = df[['Diameter (inches)', 'Topping', 'BreadType', 'Extra Topping', 'Extra Cheese']]
y = df['Price (INR)']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on Test Data
y_pred = model.predict(X_test)

# Evaluate Model Performance
print("\nModel Performance:")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):.2f}")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"R-squared (R²): {r2_score(y_test, y_pred):.2f}")

# Scatter Plot for Price vs. Pizza Diameter
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Diameter (inches)'], y=df['Price (INR)'], color='blue', label='Actual Data')
plt.xlabel('Pizza Diameter (in inches)')
plt.ylabel('Price (INR)')
plt.title('Scatter Plot: Pizza Diameter vs. Price')
plt.legend()
plt.show()

# Scatter Plot for Predicted vs. Actual Prices
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred, color='red')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs. Predicted Prices')
plt.show()

# Predicting Price for a New Pizza
new_pizza = np.array([[14, 2, 1, 1, 1]])  # Example: 14-inch, topping type 2, BreadType 1, with extra cheese & topping
predicted_price = model.predict(new_pizza)[0]
print(f"\nPredicted Price for the new pizza: ₹{predicted_price:.2f}")
