from re import S


def saberi():
    s=0
    for i in range(1,31):
       if i%3==0:
           s=s+i
           
    return s 

a=saberi()
print(a)