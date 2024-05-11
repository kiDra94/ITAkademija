'''
Forsaken by his people, he strode into the wasteland. He traveled far to the north, until he came to the great canyons. There, he founded a small village, Arroyo, where he lived out the rest of his years. And so, for a generation since its founding, Arroyo has lived in peace, its canyons sheltering it from the outside world. It is home. Your home.
'''
print("Set your appearance")
z = input("Male or \"female\" (male/female)?")
#z = input('Male or "female" (male/female)?') radi zato sto nisu isti znakovi otvorili string kao oni koji prave problem 'otvara i zatvara string, "hocu da ispise"
#z = input("Male"+"female"+"(male/female)?") --> nije praksa
if z=="male":
    print("You choose male")
else:
    print("You choose female")