#vjezba 5 ppf ex06 triangle1.py
h = 10 # u ovom slucaju je h sirina a ne visina
x = 1
for i in range(h*2):
    for j in range (x):
        print(i, end="")
    x = x + 1 if i < h-1 else x - 1
    print("")
