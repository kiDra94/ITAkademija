width   = 20
height  = 10
points  = [[2,4],[1,5],[6,6],[3,2],[0,0]]

for y in range(height):
    for x in range(width):
        print("X" if [x,y] in points else "O", end="")
    print()
