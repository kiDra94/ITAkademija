import re

txt = "(011) 234-7767"

#Check if the string contains any digits (numbers from 0-9):

#x = re.findall("\\d{2}", txt) #provjerava 2 uzastopna broj koja se pojave (ne moraju jedan do drugog biti) npr The7 rain i5n Spain9

#x = re.findall("^\\w{3,10}.\\w{3,10}@\\w{5}.\\w{2,4}$", txt) #provjera za mejl npr ukucaj  theraindgd.inspain9@gmail.com

#x = re.findall("^\(\\d{3}\)\\d{3}-\\d{4}$", txt) #trazi broj telefona (011)234-7767"

x = re.findall("^\(\\d{3}\)\s?\\d{3}-\\d{4}$", txt) # sad moze i ovako  (011) 234-7767 sa prazninom, ali samo jednom

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")