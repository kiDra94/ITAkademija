A = [[2,4,5],[1,3,7],[6,2,8]]
B = [[1,3,1],[8,9,4],[5,3,2]]
C = [[0,0,0],[0,0,0],[0,0,0]]
#Your code here
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j]= (A[i][j] + B[i][j])
print(C)

A = [[2,4,5],[1,3,7],[6,2,8]]
B = [[1,3,1],[8,9,4],[5,3,2]]
C = []

for k,v in enumerate(A):
    C.append([v[0]+B[k][0],v[1]+B[k][1],v[2]+B[k][2]]) 
    
print(C)

