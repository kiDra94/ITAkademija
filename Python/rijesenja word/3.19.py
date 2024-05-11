brojevi=[10,20,20,30,40,40,50,60,60,70,70]

originali=[]
for i in brojevi:
    if i not in originali:
        originali.append(i)
        
print(originali)