# Prvi način
import random
    
odgovor = input("Da li želite da bacite kockicu (da/ne)? ")
while odgovor == 'da':
        broj = random.randint(1, 6) #Metodom randing biramo jedan ceo broj iz zadatog opsega, u obzir ulaze i 1 i 6
        print ("Ispao je broj ", broj)
        odgovor = input("Da li želite opet da bacite kockicu (da/ne)? ")
print("Hvala, dovidjenja! ")
 
# Drugi nacin 
odgovor = input("Da li želite da bacite kockicu (da/ne)? ")
mojalista=[1,2,3,4,5,6]
while odgovor != "ne":
        print("Ispao je broj: ", random.choice(mojalista)) #Metodom choice biramo random broj iz sekvence
        odgovor = input("Da li želite opet da bacite kockicu (da/ne)? ")
print("Hvala, dovidjenja! ")