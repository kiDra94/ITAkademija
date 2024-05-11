#vjezba 4 ppf ex06 triangle.pyh 
h = 10
for i in range(1,h+1): # da krece od nule nista ne bi ispisao, posto je i 0 i j 0
    for j in range(i):
        print("#", end="") # krece uvijek od onog broja koji je trenutno i zato i izglda kao trougao
    print()
