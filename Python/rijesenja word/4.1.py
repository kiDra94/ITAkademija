def multiply(myList) :
    
    #Postavljamo vrednost promenljive rez na 1 zato sto se ta vrednost mnozi sa ostalim brojevima
    rez = 1
    for x in myList:
         rez = rez * x 
    return rez 
     

list1 = [1,2,3,4,5] 
print(multiply(list1))
