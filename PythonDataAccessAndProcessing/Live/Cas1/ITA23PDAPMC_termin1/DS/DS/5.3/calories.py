import pandas
from sklearn import linear_model
import warnings
warnings.filterwarnings("ignore")

# učitavanje podataka iz eksterne datoteke
df = pandas.read_csv("calories.csv")

# brisanje redova iz okvira za podatke koji u koloni 'Calories' umaju vrednost None
df.dropna(subset=['Calories'], inplace=True)

# count, mean, std, min, percentile, max
print(df.describe())

# ciljna kolona (target value) je kolona 'Calories'
# y je "serija" - niz podataka
y = df['Calories'] 

# atributi X se redukuju samo na 'Duration' i  'Pulse'
# x je "okvir za podatke" (može se posmatrati kao niz serija)
X = df[['Duration', 'Pulse']] # the interior brackets are for list, and the outside brackets are indexing operator
# X = df[['Duration', 'Pulse', 'Maxpulse']]

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(X)
print("-------------------")
print(y)
print("-------------------")
# print(regr.__dict__)


# predviđanje utroška kalorija kada je trajanje treninga 70 minuta i prosečni puls 105
predicted = regr.predict([[70, 105]])
# predicted = regr.predict([[70, 105, 135]])

print(predicted)
