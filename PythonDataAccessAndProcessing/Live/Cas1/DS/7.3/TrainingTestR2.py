import numpy
from sklearn.metrics import r2_score

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

# r2_score = 1 - (sum(y - predikcija)**2/sum(y - mean(y))**2)  # predikcija = mymodel(train_x)
# kada za sve vrednosti važi y = predikcija, r2_score je najveći i iznosi 1
r2_train = r2_score(train_y, mymodel(train_x))  

def r2_score_fun(y, izlaz_modela):
    suma_g = suma_d = 0
    for i in range(len(y)):
        suma_g += (y[i] - izlaz_modela[i]) ** 2
        suma_d += (y[i] - numpy.mean(y)) ** 2
    return 1 - suma_g / suma_d


print(r2_score_fun(train_y, mymodel(train_x)))
print(r2_train)

r2_test = r2_score(test_y, mymodel(test_x))
print(r2_score_fun(test_y, mymodel(test_x)))
print(r2_test)

vrednost = 5
print(f"Predikcija za x = {vrednost} je", mymodel(vrednost))




