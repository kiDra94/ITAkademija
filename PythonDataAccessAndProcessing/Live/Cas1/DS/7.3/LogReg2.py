import numpy
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import random

sluc_x = [round(random.random()*6,2) for _ in range(10000)]
# print(sluc_x)
sluc_x.sort()
X = numpy.array(sluc_x).reshape(-1, 1)
print(X.shape)

sluc_y = [random.randint(0, 1) for _ in range(10000)]
sluc_y.sort()
# print(sluc_y)
y = numpy.array(sluc_y)

logr = linear_model.LogisticRegression()
logr.fit(X, y)

# predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))
print(predicted)

confusion_matrix = metrics.confusion_matrix(y, logr.predict(X.reshape(-1, 1)))

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()

predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))
print(predicted)