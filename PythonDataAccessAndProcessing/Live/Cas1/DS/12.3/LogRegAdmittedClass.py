# importing libraries
import statsmodels.api as sm
import pandas as pd
from sklearn.metrics import (confusion_matrix, accuracy_score)
from sklearn import metrics
import matplotlib.pyplot as plt


class LogRegAdmitted:
    def __init__(self):
        self.df_train = pd.read_csv('logit_train1.csv', index_col=0)
        self.df_test = pd.read_csv('logit_test1.csv', index_col=0)

    def formiraj_trenazne_podatke(self):
        self.Xtrain = self.df_train[['gmat', 'gpa', 'work_experience']]
        self.ytrain = self.df_train['admitted']

    # building the model and fitting the data
    def napravi_model(self):
        self.log_reg = sm.Logit(self.ytrain, self.Xtrain).fit()

    def formiraj_testne_podatke(self):
        self.Xtest = self.df_test[['gmat', 'gpa', 'work_experience']]
        self.ytest = self.df_test['admitted']

    # performing predictions on the test dataset
    def napravi_predikciju(self):
        yhat = self.log_reg.predict(self.Xtest)
        print('Probabilities ', list(yhat))  # izlazne verovatnoce (round ih konvertuje u 0 ili 1)
        self.prediction = list(map(round, yhat))

    def ispisi_rezultate(self):
        print('Actual values', list(self.ytest.values))
        print('Predictions :', self.prediction)
        # accuracy score of the model
        print('Test accuracy = ', accuracy_score(self.ytest, self.prediction))

    # comparing original and predicted values of y
    def broj_promasaja(self):
        suma = 0
        zipovana_lista = list(zip(self.ytest.values, self.prediction))
        print("Zipova lista ", zipovana_lista)
        for i, j in zipovana_lista:
            suma += (i != j)
        return suma

    # confusion matrix
    def ispisi_matricu_zabune(self):
        cm = confusion_matrix(self.ytest, self.prediction)
        print("Confusion Matrix : \n", cm)

    # confusion matrix
    def vizuelno_prikazi_matricu_konfuzije(self):
        confusion_matrix = metrics.confusion_matrix(self.ytest, self.prediction)
        cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])
        cm_display.plot()
        plt.show()

    def prognoziraj_novi_podatak(self, novi_podatak):
        prognoza = self.log_reg.predict([novi_podatak])
        # print(prognoza)
        return round(prognoza[0], 3), round(prognoza[0])


if __name__ == "__main__":
    l = LogRegAdmitted()
    l.formiraj_trenazne_podatke()
    l.napravi_model()
    l.formiraj_testne_podatke()
    l.napravi_predikciju()
    l.ispisi_rezultate()
    print("Broj promasaja ", l.broj_promasaja())
    l.ispisi_matricu_zabune()
    l.vizuelno_prikazi_matricu_konfuzije()
    print(l.prognoziraj_novi_podatak([670, 3, 2]))
    print(l.prognoziraj_novi_podatak([700, 3, 7]))
