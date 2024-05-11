#fibunacijev niz rekurzivno
def fibunacijev_niz(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibunacijev_niz(n-1)+fibunacijev_niz(n-2)
print(fibunacijev_niz(3)) #nemoj prevelike broje dugo traje XD
#unapredjeno da ne radi duplo iste stvari, pogledaj sveska stablo!
def fib(n, mem):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if mem[n] != 0:
        return mem[n]
    mem[n] = fib(n-1, mem)+fib(n-2, mem)
    return mem[n]
n = 100 #sad fercera; radi do maksimalno 999!
print(fib(n, [0]*(n+1)))
#rijesenje iterativno, pamtim samo posljednja 2
def iter_fib(n):
    a = 0
    b = 1
    for i in range(2,n+1): # mora da krene od 2 posto sam prva da zadao sa a i b
        c = b + a
        a = b
        b = c
    return c 
print(iter_fib(20000))