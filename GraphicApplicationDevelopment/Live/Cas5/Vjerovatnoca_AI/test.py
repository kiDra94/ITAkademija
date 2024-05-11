import random
n = 10
a = [random.randint(0,10)*100 for _ in range(n)]
#print(a)
tsp = [[random.randint(0,10)*100 for _ in range(n)] for _ in range(n)] 
#print(tsp)

for i in range(n):
    tsp[i][i] = 0
print(tsp)

def duzine():
    tsp = [[random.randint(0,10)*100 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        tsp[i][i] = 0
    return tsp