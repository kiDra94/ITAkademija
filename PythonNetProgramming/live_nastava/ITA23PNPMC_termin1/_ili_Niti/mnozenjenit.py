import threading

A = [[12,7,3],
    [4,5,6],
    [7,8,9]]

B = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

class MyThread(threading.Thread):

    def __init__(self,i,j):
        threading.Thread.__init__(self)
        self.i = i
        self.j = j
    
    def run(self): #run se ne poziva direktno, nego preko start kod nit!!!
        print("running")
        print("Nit ", self.i, " ", self.j)
        for k in range(len(B)): 
            result[self.i][self.j] = A[self.i][k] * B[self.i][j]

t = []
for i in range(len(A)):
    t.append([])
    for j in range(len(B[0])):
        t[i].append(MyThread(i,j))
print(t)
for i in range(len(A)):
    for j in range(len(B[0])):
        t[i][j].start()
        t[i][j].join() #zakomentarisi pa ne radi
        #pass

for r in result:
    print(r)