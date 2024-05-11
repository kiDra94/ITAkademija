
x=int(input('Unesite ceo broj: '))

t=True      
    
if (x==1):             
    t = False       

for i in range(2,x):   
    if (x%i == 0):     
        t = False   
 

if t:
    print('DA')
else:
    print("NE")