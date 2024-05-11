import random as rd
print(rd.randint(3, 9)) #int izmedju 3 i 9
print(rd.random()) # 0-1 float
print(rd.random()*9) # broj nikad nece preci 9
print(rd.random()*6+3) # raspon, mnozim sa razlikom; ide od 6 do 6+3
a = 3
b = 19
print(rd.random()+(b-a)+a) #float brojevi izmedju a i b!!!