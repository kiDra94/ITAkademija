import pandas
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

scale = StandardScaler() # standardizacija ((X-mean)/std)

df = pandas.read_csv("co_emission.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']
print(X)
print("------------------------")

scaledX = scale.fit_transform(X)
print(scaledX)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1300]])
print("------------------------")
print(scaled)

predictedCO2 = regr.predict(scaled)
print(predictedCO2)

print("PROVERA SKALIRANIH VREDNOSTI")

# list of values of 'Weight' column
marks_list = df['Weight'].tolist()

# show the list
print(marks_list)

skalirane = [(i - np.mean(marks_list))/np.std(marks_list) for i in marks_list]
print(skalirane)

plt.hist(marks_list, 100)
plt.show()

plt.hist(skalirane, 100)
plt.show()
