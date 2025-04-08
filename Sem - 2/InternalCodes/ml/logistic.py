import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # To split data
from sklearn.linear_model import LogisticRegression  # Logistic Regression model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # Metrics

# Load dataset
data = pd.read_csv("sample_dataset.csv")  # Make sure this file exists in the same folder

# Show first few rows
print("First few rows of the dataset:")
print(data.head())

# Separate features and target
X = data.drop("purchased", axis=1)  # All columns except 'purchased'
y = data["purchased"].astype(int)   # Ensure target is categorical (0 or 1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize logistic regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluation metrics
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
