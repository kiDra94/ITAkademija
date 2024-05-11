a = []*3
print(a)
b = [[]*3]*3
print(b)
b[0].append(1) # OPREZ
print(b)
 
d=[[],[],[]]
print(d)
d[0].append(1)
print(d)
 
print("------------------------")
 
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
 
print("Matrix =", matrix)
 
'''
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Initialize matrix
matrix = []
print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries
for row in range(Row):
    a = []
    # A for loop for column entries
    for column in range(Column):
        a.append(int(input()))
    matrix.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print() 
'''
 
print("---------------------")
 
matrix = [[column for column in range(4)] for row in range(4)]
print(matrix)
 
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = column = 1
X[row][column] = 11
print(X)
 
print(X[:2])
print(X[:2][:1]) # [[1, 2, 3]]
print(X[:2][:1][0]) # [1, 2, 3]
print(X[:2][:1][0][:2]) #[1 2]
 
row = -2
column = -1
X[row][column] = 21
print(X)
 
print("Matrix at 1 row and 3 column=", X[0][2])
print("Matrix at 3 row and 3 column=", X[2][2])
print(X[0:2][0][0:2])
 
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(X[-1][-2])
 
# Program to add two matrices using nested loop
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
 
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
# iterate through rows
for row in range(len(X)):
 
    # iterate through columns
    for column in range(len(X[0])):
        result[row][column] = X[row][column] + Y[row][column]
 
for r in result:
    print(r)
 
 
 
Add_result = [[X[row][column] + Y[row][column]
               for column in range(len(X[0]))]
              for row in range(len(X))]
Sub_result = [[X[row][column] - Y[row][column]
               for column in range(len(X[0]))]
              for row in range(len(X))]
 
print("Matrix Addition")
for r in Add_result:
    print(r)
 
print("\nMatrix Subtraction")
for r in Sub_result:
    print(r)
 
rmatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
for row in range(len(X)):
    for column in range(len(X[0])):
        rmatrix[row][column] = X[row][column] * Y[row][column]
 
print("Matrix Multiplication", )
for r in rmatrix:
    print(r)
 
for i in range(len(X)):
    for j in range(len(X[0])):
        rmatrix[row][column] = X[row][column] // Y[row][column]
 
print("\nMatrix Division", )
for r in rmatrix:
    print(r)
 
X = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
 
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
# iterate through rows
for row in range(len(X)):
    # iterate through columns
    for column in range(len(X[0])):
        result[column][row] = X[row][column]
 
for r in result:
    print(r)