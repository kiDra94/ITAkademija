import numpy
import matplotlib.pyplot as plt

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

train_x = x[:80]
train_y = y[:80]

plt.scatter(train_x, train_y, color='green')
plt.show()

test_x = x[80:]
test_y = y[80:]

plt.scatter(test_x, test_y, color='red')
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

