a=float(input("Unesite realan broj: "))

if (a>=0 and a<51):
    print("Student je pao ispit")
elif(a>=51 and a<61):
    print("Student je dobio ocenu 6")
elif(a>=61 and a<71):
    print("Student je dobio ocenu 7")
elif(a>=71 and a<81):
    print("Student je dobio ocenu 8")
elif(a>=81 and a<91):
    print("Student je dobio ocenu 9")
elif(a>=91 and a<=100):
    print("Student je dobio ocenu 10")
else:
    print("Broj bodova nije korektan")
