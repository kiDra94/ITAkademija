from re import S


def make():
    s=''
    i=1
    while i<10:
        s=s+str(i)+'.'
        i+=1
    print(s)
    
make()
print(type(make()))