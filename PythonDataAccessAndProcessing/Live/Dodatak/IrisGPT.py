import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Load the iris dataset
iris = load_iris()
print(iris)
X = iris.data
print(X)
y = iris.target
print(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the KNeighborsClassifier
# ostavi samo jedan knn!!, ostale zakomnentarisi, ovo su razliciti algoritmi
knn = KNeighborsClassifier()
knn = DecisionTreeClassifier()
knn = linear_model.LogisticRegression()
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Calculate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()