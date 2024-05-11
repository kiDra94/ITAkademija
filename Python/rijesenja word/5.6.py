#prvi nacin
f=open('izlaz.txt','w')

for i in range(1,21):
    if i%2==0:
        f.write(str(i)+'\n')
f.close()


#drugi nacin
with open('izlaz.txt','w') as f:
    for i in range(1,21):
        if i%2==0:
            f.write(str(i)+'\n')
