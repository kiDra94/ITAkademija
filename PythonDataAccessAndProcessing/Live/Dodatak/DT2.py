import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import neighbors
import numpy as np
from sklearn import metrics
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

df = pandas.read_csv("shows.csv")
print(df)

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
print(X)
y = df['Go']
print(y)

#decision_tree = DecisionTreeClassifier()
decision_tree = LogisticRegression(random_state=0)
#decision_tree = KNeighborsClassifier()
decision_tree = decision_tree.fit(X, y)

# 5. Splitting training and testing data
features_train, features_test, label_train, label_test = model_selection.train_test_split(
    X,
    y,
    test_size=0.2
)

print('Model score: ', decision_tree.score(features_test, label_test))
print(features_test)
print(label_test)
print('\n')


'''
from sklearn.tree import plot_tree
plt.figure(figsize=(10,10))
plot_tree(decision_tree, filled=True)
plt.savefig("DT.png")
plt.show()'''



