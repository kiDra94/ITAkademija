def napuni_listu(n):
    lista = [i if i % 2 != 0 else -i for i in range(1, n+1)]
    return lista

def napuni_listu1(n, znak):
    lista1 = []
    #i if i % 2 else -i for i in range(1, n + 1)
    for i in range(1, n+1):
        lista1.append(i*znak)
        znak = -znak
    return lista1

n = 30
znak = 1
print(napuni_listu(n))
ll = napuni_listu1(n,1)
print(napuni_listu1(n, znak))


