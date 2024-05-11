N = 7
def formiraj_matricu():
    return [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    '''
    #ovo je drugo rijesenje!
    mat = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        mat[i][i] = 1
    return mat
    '''
        
def ispis_matricu(mat):
    for i in mat:
        print(i)

#print(formiraj_matricu())
ispis_matricu(formiraj_matricu())
