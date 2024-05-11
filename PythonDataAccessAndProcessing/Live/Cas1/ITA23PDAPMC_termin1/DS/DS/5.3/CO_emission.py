import pandas
from sklearn import linear_model
import warnings
warnings.filterwarnings("ignore")

df = pandas.read_csv("co_emission.csv")

# count, mean, std, min, percentile, max
print(df.describe())

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# The coefficient is a factor that describes the relationship with an unknown variable.
print(regr.coef_)

# predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

predictedCO2 = regr.predict([[3300, 1300]])

# povećanje za (3300-2300)*regr.coef_
print(predictedCO2)