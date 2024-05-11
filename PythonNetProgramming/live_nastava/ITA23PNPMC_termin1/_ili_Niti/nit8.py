import threading  
import time 
  
obj1= threading.Condition() 


def task (): 
  
  print('addition of 1 to 10000000 ') 
  #add= 0
  global add
  for i in range (1, 10000001):
    add = add+1 
  print('the condition object is releases now') 
    
add=0
time.sleep(1)
t1 = threading.Thread(target = task) 
t2 = threading.Thread(target = task) 
t1.start() 
t2.start()
t1.join() 
t2.join()
print(add) 
'''bez join; glavna nit ne ceka i onda se ne zavrsava sporedna nit kako treba i kriticna sekcija se narusava 
(to znaci da ne dodavanje ne vraca nazad u add)'''

print("---------------------------")