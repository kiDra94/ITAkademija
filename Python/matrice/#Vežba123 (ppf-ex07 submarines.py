#Vežba (ppf-ex07 submarines.py)
'''m = 10
submariens = [3,5,3,6,7,6,8,6,2,1,2,2]
sub = []
for y in range(m):
    for x in range(m):
        print("*" if y == 0 or x == 0 or y == m-1 or x == m-1 else " ", end="")
        for subs, i in enumerate(submariens):
            x1, y1, x2 ,y2 = submariens[i:i+4]
            if x1 == x and y1 == y or x2 == y or y2 == y:
                print(subs, end=" ")
    print("")'''

m = 10
submariens = [3, 5, 3, 6, 7, 6, 8, 6, 2, 1, 2, 2]

for y in range(m):
    for x in range(m):
        submarine_number = None
        for i in range(0, len(submariens), 4):
            x1, y1, x2, y2 = submariens[i:i + 4]
            if (x1 == x and y1 == y) or (x2 == x and y2 == y):
                submarine_number = i // 4
                break

        print(submarine_number if submarine_number is not None else "*", end=" ")

    print("")