N = 10

def obrada(N):
    return [[1 if i == 0 or i == N-1 or j == 0 or j == N-1 else 0 for j in range(N)] for i in range(N)]

def ispis(mat):
    for r in mat:
        print(r)

ispis(obrada(N))

print("-----------------------------------")

mat1 = []
for i in range(N):
    red = []
    for j in range(N):
        if(i == 0 or i == N-1 or j == 0 or j == N-1):
            red.append(1)
        else:
            red.append(0)
    mat1.append(red)

ispis(mat1)