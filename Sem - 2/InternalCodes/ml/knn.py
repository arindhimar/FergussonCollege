import pandas as pd  # Import pandas for data manipulation
from sklearn.model_selection import train_test_split  # Import function to split data into train and test sets
from sklearn.neighbors import KNeighborsClassifier  # Import KNN classifier from sklearn
from sklearn.metrics import accuracy_score  # Import accuracy metric to evaluate model

data = pd.read_csv("file_path")

print(data.head())

X = data.iloc[:, :-1]
y = data.iloc[:, -1]  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
