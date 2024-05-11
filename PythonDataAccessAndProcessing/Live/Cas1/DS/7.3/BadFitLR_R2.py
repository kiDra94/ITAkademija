import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
import numpy

x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(slope)  # 0.01391658139845263
print(r)  # 0.01331814154297491


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))
print(mymodel)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


mymodel = numpy.poly1d(numpy.polyfit(x, y, 4)) # svodi se na prethodno ako je: mymodel = numpy.poly1d(numpy.polyfit(x, y, 1))
print(mymodel)
plt.scatter(x, y)

myline = numpy.linspace(0, 100, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()


print("r2_score: ", r2_score(y, mymodel(x)))
