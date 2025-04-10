import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # To split data
from sklearn.linear_model import LinearRegression  # Import Linear Regression model
from sklearn.metrics import mean_squared_error, r2_score  # Regression metrics

# Load dataset
data = pd.read_csv("sample_dataset.csv")  # Replace with your actual file path

# Split features and target
X = data.iloc[:, :-1]  # All columns except the last as features
y = data.iloc[:, -1]   # Last column as target

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")
