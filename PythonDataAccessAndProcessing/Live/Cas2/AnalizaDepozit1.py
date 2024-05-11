import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns #sluzi za davanje parametara kad crta
import warnings

warnings.filterwarnings('ignore')

sns.set_theme(style="white") # deprecated znaci zastarjelo; kad stoji sns.set
sns.set_theme(style="whitegrid", color_codes=True)

data = pd.read_csv('banking.csv', header=0)
# print(data.head()) # ucitava prvih 5 redova
# print(data.tail()) # posljdnjih 5 redova
# print(data.shape) #stanje frejma (41188, 21)
data = data.dropna() # brise none vrijednosti
# print(data.shape) # zakljucak da nema none vriednosti; cisti su podaci

#od 24
print(data['education'])

print(data['education'].unique())

data['education'] = np.where(data['education'] == 'basic.9y', 'Basic', data['education']) # where je ugradjen u np biblitiku
data['education'] = np.where(data['education'] == 'basic.6y', 'Basic', data['education'])
data['education'] = np.where(data['education'] == 'basic.4y', 'Basic', data['education'])

print(data['education'].unique())
'''
print(data['education'].value_counts()) # pokazuje koliko podataka koja kolona ima!
print(data['y'].value_counts())

for i in data:
    print(data[i].value_counts())'''

#38-39
#pita kad je negdje null tj none pisace true!
null_df = data.isnull()
# print(null_df)


#36-41 vizualni prikaz
sns.countplot(x='y', data=data, palette='hls') # 'y' je ime kolone!!!
plt.savefig('count_plot.png') # snima sliku
# plt.show() # prikazuje

sns.countplot(x='marital', data=data, palette='hls')
plt.savefig('count_plot_marital.png') 
# plt.show()

'''#52-59
print("-----------------")
print(data.groupby('y')['y'].mean()) 
print("-----------------")
print(data.groupby('marital')['y'].mean()) # grupise sve u odnosu na 'y' i onda daje airtmeticku sredinu izmejdu razvedenih
print("-----------------")
print(data.groupby('age')['y'].mean()) 
print("-----------------")'''

#61-69
pd.crosstab(data.job, data.y).plot(kind='bar')
plt.title('Purchase Frequency for Job Title')
plt.xlabel('Job')
plt.ylabel('Frequency of Purchase')
plt.savefig('purchase_fre_job.png')
# plt.show()

#68-74
table = pd.crosstab(data.marital, data.y)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Marital Status vs Purchase')
plt.xlabel('Marital Status')
plt.ylabel('Proportion of Customers')
plt.savefig('mariral_vs_pur_stack.png')
# plt.show()

print("------------------------------")

#112-117
#izdvojenje kolone koje nisu numerativne
cat_vars = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']
for var in cat_vars: 
    cat_list = 'var' + '_' + var # var koje nije zakomentarisano uzima vrijednosti iz kolona
    cat_list = pd.get_dummies(data[var], prefix=var) #previx = var dodaje ime kolone prije "_"
    data1 = data.join(cat_list) # spaja sve u jedan string!
    data = data1
print(data.columns)
# print(data)
# da prebacimo true false u numericke vrijednosti
data = data.replace({True: 1, False: 0})
# print(data)
# print("-----------------------------")
# print(data['day_of_week_thu']) #uglavnom se ovo koristi!
# print("ovo gore i ispod radi isto!")
# print(data.day_of_week_thu)
# print(type(data)) #tip je dataframe

#123-130

cat_vars = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']
data_vars = data.columns.values.tolist() #to list pravi listu!
to_keep = [i for i in data_vars if i not in cat_vars]
print(to_keep) #bacamo sve one od kojih smo napravili dummies, osim numerickih posto od njih nisu pravljeni dummies
print("----------------------")
data_final = data[to_keep] # ovo je bio cilj, da napravimo datafram koji ima numericke kolone i od ostalih kolona dummies
print(data_final)
print("-----------------------")
print(data_final.columns.values)
#  print(data_final.to_string())
print("-----------------------")
#132-136
data_final_vars = data_final.columns.values.tolist()
y = ['y']
print(y)  # ciljna kolona
X = [i for i in data_final_vars if i not in y] #odvaja atribute od ciljne kolone
print(X)  # atributi

#138-148
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
#  rfe = RFE(logreg, step=18)
rfe = RFE(logreg) # REF -> algoritam sam odlucuje koje kolone nisu informativne!
rfe = rfe.fit(data_final[X], data_final[y])
print(rfe.support_) # ispisuje koje kolone je uzeo
print(rfe.ranking_) # kako ih je rankirao
print("---------------------------")
#150-163
from itertools import compress

izabrani = list(compress(X, rfe.support_))
print(izabrani)
print("---------------------------")
X = data_final[izabrani]
y = data_final['y']
print(X)

#165-170
#pravljenje i fitovanje modela tj analiza podatka koje do sad imamo
import statsmodels.api as sm
logit_model = sm.Logit(y, X)
result = logit_model.fit()

#172-188
#pravljenje predikcije
#y_test znamo i to poredimo sa y_pred da vidimo da li je model ispravan
#u pirntu ce nam dati tacnost tj skor
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0) #uzimamo 30% podataka za test!
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

from sklearn import model_selection
from sklearn.model_selection import cross_val_score
kfold = model_selection.KFold(n_splits=10, random_state=7, shuffle=True)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))

#190-213 Matrica konfuzije
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
 
cm_display.plot()
plt.show()
