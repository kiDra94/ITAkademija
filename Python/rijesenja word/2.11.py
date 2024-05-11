#prvi način
i=1
while(i<=30):
    #Ako ostatak pri deljenju sa 3 nije 0 onda broj nije deljiv sa 3
    if(i%3!=0):
        print(i)
    i=i+1


#drugi način
for i in range(1,31):
    #Ako je ostatak pri deljenju sa 3 nula onda je broj deljiv sa 3 i tada se vracamo na pocetak petlje 
    if (i%3==0):
        continue
    print(i)
