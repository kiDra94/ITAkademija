N = 10

mat = [[1 if i == 0 or i == N-1 or j == 0 or j == N-1 else 0 for j in range(N)] for i in range(N)]

for r in mat:
    print(r)

for i in range(N):
    for j in range(N):
        if(i == 0 or i == N-1 or j == 0 or j == N-1):
            print("1", end="")
        else:
            print("0", end="")
    print("")