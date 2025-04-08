import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # To split data
from sklearn.linear_model import LogisticRegression  # Logistic Regression model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # Metrics

# Load dataset
data = pd.read_csv("file_path")  # Replace with your actual file path

# Show first few rows
print(data.head())

# Feature matrix and target vector
X = data.iloc[:, :-1]  # All columns except last
y = data.iloc[:, -1]   # Last column as target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression(max_iter=1000)  # max_iter is increased in case of convergence issues
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluation
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
