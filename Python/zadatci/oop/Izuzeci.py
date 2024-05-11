a = 5
b = 0
if a == 3:
    raise ZeroDivisionError
    b = a/(a-3) 
print("Value of b = ", b)
a = 3
try:
    if a == 3:
        #raise ZeroDivisionError #greska se sama od sebe desava i except ce da je obradi!
        b = a/(a-3) 
    print("Value of b = ", b)
except ZeroDivisionError:
    print("An error occurred")
print("Value of b = ", b)
print("-----------------------")
try:
    if a == 3:
        pass
        #raise ZeroDivisionError
        #b = a/(a-3) #zakomentarisati posto ce stati kod ove greske!
    print("Value of b = ", b)
    a = [1, 2, 3]  
    print("Second element = %d" %(a[3])) #izbacuje gresku IndexError
except (ZeroDivisionError,IndexError): #mogu se navesiti vise gresaka
    print("An error occurred")
print("Value of b = ", b)
print("-----------------------")
#rijesenje da se svaki error ispise!
a = 3 
b = 0
try:
    if a == 3:
        b = a/(a-3) 
    print("Value of b = ", b)
except (ZeroDivisionError): 
    print("An error occurred - zero division")
try:
    a = [1, 2, 3]  
    print("Second element = %d" %(a[3])) #izbacuje gresku IndexError
except IndexError:
    print("An error occurred - index out of range")
except Exception: #pokriva sve ostale greske, posto je to roditelj
    print("An error occurred - big error")
print("Value of b = ", b)
#help(IndexError) #ispisuje porodicno stablo svakog objekta!!!!
print("-----------------------")