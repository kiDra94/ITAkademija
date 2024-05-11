import pandas
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
# https://towardsdatascience.com/a-look-at-precision-recall-and-f1-score-36b5fd0dd3ec
# https://medium.com/@nirajan.acharya666/understanding-precision-recall-f1-score-and-support-in-machine-learning-evaluation-7ec935e8512e

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

data_frame = pandas.read_csv('car.data')

labels = {
    'Buying': ['vhigh', 'high', 'med', 'low'],
    'Maintenance': ['vhigh', 'high', 'med', 'low'],
    'Doors': ['2', '3', '4', '5more'],
    'Persons': ['2', '4', 'more'],
    'LuggageBoot': ['small', 'med', 'big'],
    'Safety': ['low', 'med', 'high'],
    'Class': ['unacc', 'acc', 'good', 'vgood']
}

#cisti podate, dodjeluje numericke vrijedosti
label_encoders = {}
data_frame_encoded = pandas.DataFrame()
for column in data_frame:
    if column in labels:
        label_encoders[column] = preprocessing.LabelEncoder()
        label_encoders[column].fit(labels[column])
        data_frame_encoded[column] = label_encoders[column].transform(
            data_frame[column])
    else:
        data_frame_encoded[column] = data_frame[column]

# print(data_frame_encoded)

#futers trenazni i testni podaci; label ciljna kolona
features = np.array(data_frame_encoded.drop(['Class'], axis=1))
label = np.array(data_frame_encoded['Class'])
#podjela na trenazne i testne podatke
features_train, features_test, label_train, label_test = model_selection.train_test_split(
    features,
    label,
    test_size=0.1
)
#odluka koji algoritam koristimo
decision_tree = DecisionTreeClassifier() # precizniji!
#decision_tree = KNeighborsClassifier()
decision_tree.fit(features_train, label_train)

print('Score: ', decision_tree.score(features_test, label_test))
#print(features_test.flatten())
#print(label_test)
print('\n\n')
print(
    classification_report(
        label_test,
        decision_tree.predict(features_test)
    )
)
