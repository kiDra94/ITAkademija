import pandas
from sklearn import linear_model
import warnings
warnings.filterwarnings("ignore")

df = pandas.read_csv(r"C:\Users\OEM\Desktop\IT Akademija\PythonDataAccessAndProcessing\Live\Cas1\DS\5.3\co_emission.csv")

#print(df) #iscit fajl!
#print(df.head()) #ispisuje prvih 5
#print(df.tail()) #ispisuje posljednjih 5
# count, mean, std, min, percentile, max
#print(df.describe())

X = df[['Weight', 'Volume']] #navodimo koje kolone hocemo da iscupamo
#print(X)
y = df['CO2']
#print(y)


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