import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # To split data
from sklearn.ensemble import RandomForestClassifier  # Random Forest model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # Evaluation metrics

# Load the dataset
data = pd.read_csv("file_path")  # Replace with your actual file path

# Show first few rows
print(data.head())

# Split into features and target
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Random Forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)

# Evaluate model
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
