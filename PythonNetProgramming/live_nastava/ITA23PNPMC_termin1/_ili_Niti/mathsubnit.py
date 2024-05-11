#zadatak da jedna nit racuna jednu vrstz, druga drugu itd.
'''
[9,8,7]   [1,2,3]    [10,10,..]
[6,5,4] + [4,5,6]  = [10,..,..] 
[3,2,1]   [7,8,9]    [10,..,..]
ovako da racuna (prvo jedna nit prvo mjesto, pa druga nit drugo mjesto, pa treca nit trece mjesto!!!)
'''
import threading

X = [[1,2,3],
    [4,5,6],
    [7,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[0,0,0],
    [0,0,0],
    [0,0,0]]

class MyThread(threading.Thread):

    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i = i
    
    def run(self): #run se ne poziva direktno, nego preko start kod nit!!!
        print("running")
        print("Nit ", self.i)
        for j in range(len(X[i])): #ako sotji samo X, onda radi samo kad su kvadratne matrice tj x i y isto!!!
            result[self.i][j] = X[self.i][j] + Y[self.i][j]

t = []

for i in range(len(X)):
    t.append(MyThread(i))
print(t)
for i in range(len(X)):
    t[i].start()
    t[i].join() #zakomentarisati, pa glavna nece cekati i dolazi do problema!
    #pass
for r in result:
    print(r)
#zadatak mnozenje matrica sa nit i bez!; kad se radi sa nit treba nam 9 niti
'''
[9,8,7]   [1,2,3]    [10,10,..]
[6,5,4] + [4,5,6]  = [10,..,..] 
[3,2,1]   [7,8,9]    [10,..,..]
matrica se mnozi -> [9,8,7] * [1,4,7] (1*9)+(8*4)+(7*7) -> [9,32,49] je prva vrsta!
matrica se mnozi -> [6,5,4] * [2,5,8] (6*2)+(5*5)+(4*8) -> [12,25,32] je druga vrsta!
matrica se mnozi -> [3,2,1] * [3,6,9] (3*3)+(2*6)+(1*9) -> [9,12,9] je treca vrsta!
'''
#modifikuj da radi ovo iznad
X = [[1,2,3],
    [4,5,6],
    [7,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[i])):
        result[i][j] = X[i][j] + Y[i][j]
print(result)
print("---------")
for i in range(len(result)):
    print(f"{result[i]}")
print("---------")
for i in result:
    print(i)