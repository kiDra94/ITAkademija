import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


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

decision_tree = DecisionTreeClassifier()
decision_tree = decision_tree.fit(X, y)

from sklearn.tree import plot_tree
plt.figure(figsize=(10,10))
plot_tree(decision_tree, filled=True)
plt.show()
