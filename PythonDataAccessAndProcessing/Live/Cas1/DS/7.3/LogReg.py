import numpy
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt

#duzina tumora; sto duzi to losije po covjeka
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88])
print(X.shape)

# Reshaped for Logistic function. Dodaje drugu dimenziju!
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
print(X.shape)
# y daje za X veijdnost TRUE ili FALSE; tj u ovom slucaju opasan po covjeka ili ne
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X, y)

# predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))
print(predicted)

# In logistic regression the coefficient is the expected change in log-odds of having the outcome per unit change in X.
log_odds = logr.coef_
odds = numpy.exp(log_odds) #izlaz iz linearne regresije

# This tells us that as the size of a tumor increases by 1mm the odds of it being a cancerous tumor increases by 4x.
print(odds)  # [4.03541657]

# funkcija p = exp(y)/(exp(y)+1) dobro opisuje verovatnoću (y = logr.coef_ * X + logr.intercept_)
# važi 0<p<1 i dodatno kako X raste p teži ka 1 i obrnuto, kada X opada (u minusu) p teži ka nuli
# za X=0, p=1/2
def logit2prob(logr, X):
    log_odds = logr.coef_ * X + logr.intercept_
    odds = numpy.exp(log_odds)
    probability = odds / (1 + odds)
    return probability

# Find the log-odds for each observation
print(logit2prob(logr, X))
predikcija = [0 if i < 0.5 else 1 for i in logit2prob(logr, X)] # za p>=1/2 prihvatamo da je izlaz (predikcija) 1 (True) (u suprotnom je 0 (False))
print("Stvarne vrednosti: ",list(y))
print("Predikcija: ",predikcija)

# prikaz matrice zabune
confusion_matrix = metrics.confusion_matrix(y, logr.predict(X.reshape(-1, 1)))
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])
cm_display.plot()
plt.show()
