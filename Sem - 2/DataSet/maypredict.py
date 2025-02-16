import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset (replace with your CSV path)
df = pd.read_csv("pizza_dataset_extended.csv")

# 1. Exploratory Data Analysis (EDA)
print("First 5 rows:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Correlation Analysis (Numerical Variables)
numerical_cols = ['Pizza Diameter', 'Price (INR)']
correlation_matrix = df[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 3. Visualize Relationships with Scatter Plots
sns.scatterplot(data=df, x='Pizza Diameter', y='Price (INR)', hue='BreadType')
plt.title("Price vs. Diameter by BreadType")
plt.show()

sns.boxplot(data=df, x='BreadType', y='Price (INR)')
plt.title("Price Distribution by BreadType")
plt.show()

# 4. Prepare Data for Linear Regression
# Encode categorical variables (One-Hot Encoding)
df_encoded = pd.get_dummies(df, columns=['Topping', 'BreadType'], drop_first=True)

# Split data into features (X) and target (y)
X = df_encoded.drop('Price (INR)', axis=1)
y = df_encoded['Price (INR)']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Evaluate Model
y_pred = model.predict(X_test)

print("\nModel Performance:")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

# 7. Visualize Predictions vs Actual
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Price (INR)")
plt.ylabel("Predicted Price (INR)")
plt.title("Actual vs. Predicted Prices")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)  # Diagonal line
plt.show()

# 8. Feature Importance
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', ascending=False)

print("\nFeature Importance:")
print(coefficients)

# 9. Predict Price for a New Pizza
def predict_pizza_price():
    new_pizza = {
        'Pizza Diameter': 14,
        'Extra Toppings': True,
        'Extra Cheese': True,
        'Topping_Pepperoni': 1,  # One-hot encoded
        'BreadType_Thick': 1      # One-hot encoded
    }
    new_df = pd.DataFrame([new_pizza]).reindex(columns=X.columns, fill_value=0)
    predicted_price = model.predict(new_df)
    print(f"\nPredicted Price: ₹{predicted_price[0]:.2f}")

predict_pizza_price()