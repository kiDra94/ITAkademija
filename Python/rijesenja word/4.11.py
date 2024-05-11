x=[]

for i in range(1,10):
    x.append(i)
    
number_iterator = iter(x) 
  
while number_iterator: 
    try: 
        print(next(number_iterator)) 
  
    except StopIteration: 
        break