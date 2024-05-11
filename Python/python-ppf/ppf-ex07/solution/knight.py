start = [int(input("x: ")),int(input("y: "))] 

available = [
    [start[0]-1,start[1]-2],
    [start[0]-2,start[1]-1],
    [start[0]+1,start[1]-2],
    [start[0]+2,start[1]-1],
    [start[0]-1,start[1]+2],
    [start[0]-2,start[1]+1],
    [start[0]+1,start[1]+2],
    [start[0]+2,start[1]+1]
] 

used_positions = 0

letters = ['A','B','C','D','E','F','G','H']
for y in range(8):
    print(y+1,end=" ")
    for x in range(8):
        chr = "O"
        if [x+1,y+1] == start:
            chr = "S"
        if [x+1,y+1] in available:
            used_positions+=1
            chr = "M"
        print(chr,end="")
    print()
print(end="  ")
for l in letters:
    print(l,end="")
print()

print("Possible positions:",used_positions)