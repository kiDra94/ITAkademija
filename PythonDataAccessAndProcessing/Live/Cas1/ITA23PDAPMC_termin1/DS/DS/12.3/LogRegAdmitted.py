# importing libraries
import statsmodels.api as sm
import pandas as pd

# loading the training dataset
df = pd.read_csv('logit_train1.csv', index_col=0)
print(df)

# defining the dependent and independent variables
Xtrain = df[['gmat', 'gpa', 'work_experience']]
print(Xtrain)
ytrain = df['admitted']
print("----------------------")
print(ytrain)

# building the model and fitting the data
log_reg = sm.Logit(ytrain, Xtrain).fit()

# printing the summary table
# print(log_reg.summary())

# loading the testing dataset
df = pd.read_csv('logit_test1.csv', index_col=0)

# defining the dependent and independent variables
Xtest = df[['gmat', 'gpa', 'work_experience']]
ytest = df['admitted']

# performing predictions on the test dataset
yhat = log_reg.predict(Xtest)
print(list(yhat)) # izlazne verovatnoce (round ih konvertuje u 0 ili 1)
prediction = list(map(round, yhat))

# comparing original and predicted values of y
print('Actual values', list(ytest.values))
print('Predictions :', prediction)

from sklearn.metrics import (confusion_matrix, accuracy_score)

# confusion matrix
cm = confusion_matrix(ytest, prediction)
print("Confusion Matrix : \n", cm)

# accuracy score of the model
print('Test accuracy = ', accuracy_score(ytest, prediction))

from sklearn import metrics
import matplotlib.pyplot as plt

# confusion matrix
confusion_matrix = metrics.confusion_matrix(ytest, prediction)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])
cm_display.plot()
plt.show()

novi_podatak = [670, 3, 2]
prognoza = log_reg.predict([novi_podatak])
print(prognoza, round(prognoza[0]))

novi_podatak = [700, 3, 7]
prognoza = log_reg.predict([novi_podatak])
print(prognoza, round(prognoza[0]))