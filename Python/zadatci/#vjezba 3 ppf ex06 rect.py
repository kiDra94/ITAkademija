#vjezba 3 ppf ex06 rect.py
h = 5
w = 10
for i in range(1,h+1): # da krece od 0 isousai bi 6 znakova, nula se racuna
    for j in range(1,w+1):
        if i==1 or i==h or j==1 or j==w: # mora da ide do h posto h+1 nepostoji zadnji se ne cita
            print("#", end="")
        else:
            print(" ", end="")
    print()
print()