import math as m
from random import randint
def kvadratna_jednacina(a, b, c):
    if a == 0:
        return(-c/b,)
    else:
        D = (b*b) - (4*a*c)
        if D<0:
            return None
        elif D==0:
            return(-b/(2*a),)
        else:
            return((-b - m.sqrt(D))/(2*a), (-b + m.sqrt(D))/(2*a))
    

if __name__ == "__main__":
    #ovako sami sebi mozemo da kreiaramo assertove
    for i in range(20):
        (a, b, c) = (randint(-100, 100)), (randint(-100, 100)), (randint(-100, 100))
        print((a, b, c), "==", kvadratna_jednacina(a, b, c))

    assert kvadratna_jednacina(1, 6, 5) == (-5, -1)
    assert kvadratna_jednacina(1, 4, 4) == (-2,)
    assert kvadratna_jednacina(1, 6, 45) is None
    assert kvadratna_jednacina(0, 2, 2) == (-1,)