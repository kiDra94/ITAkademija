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
# print(data)
# slajsovnje! --> ovo  from sklearn.model_selection import train_test_split djeli fajl na trenazne i rest podatke; 
# trenazni za treniranje modela, test za testiranje; to automatksi radi slajsiranje
trening = data[:32000]
rest = data[32000:]
# print(data.columns)
''' #for petlja uzima isto imena colona
for i in data:
    print(i)'''
# print(data['age']) # ispisuje samo kolonu age
# print(data['age'].to_string) #ispisuje sve, zato sto pravi string; ne koristi se cisto da znamo
# print(data[['age', 'marital', 'job']]) # moraju 2 vicistae zagrade, zato sto ocekuje listu, redosljed nebitan, ispisuje kako je zadano!
# print(data['marital'].values)
# print(set(data['marital'].values)) # vraca vrijednosti koje se nalaze u koloni, set da bi obrisao duplikate kako bi sve vidjeli
# print(list(set(data['marital'].values))) # ako hocemo da opet bude lista -> ima vise mogucnosti; npr for petlja moze da ide korz listu a ne korz skup
# print(data['marital'].unique()) # isto nacin da se ispise bez duplikata
''' # iscitavanje svih unique vrjednosti (od svake kolone)
for i in data:
    print(data[i].unique())'''
# print(pd.get_dummies(data['marital'])) # pretvara vrijednost u true i false vrijednsoti; pravi vise kolone!
# print(pd.get_dummies(data['age']))
# print(pd.get_dummies(data[['job', 'marital']])) # radi i sa vise kolona; NAPOMENA: ako stavis age, bice samo ispisano zato sto je vec broj!
data2 = pd.get_dummies(data[['job', 'marital']])
print(data2.columns)

