
s1={2,3,5,7,11,13,17,19,23,29}
s2={0,1,1,2,3,5,8,13,21,34}

print("Unija: ",s1 | s2)
print("Presek: ",s1 & s2)
print("Razlika (s1/s2)", s1-s2)
print("Razlika (s2/s1)", s2-s1)

s1.remove(2)    #Ako prosleđeni element ne postoji u skupu dobićemo grešku 
s2.discard(1)   #Ako prosleđeni element ne postoji u skupu nećemo dobiti grešku 


print("Skup 1: ",s1)
print("Skup 2: ",s2)
