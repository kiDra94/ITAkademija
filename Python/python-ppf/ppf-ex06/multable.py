rows = int(input("Enter number: "))

print('1\t2\t3')
print('********************')
for i in range(1,rows+1):
    print(i*1,end='')
    print('\t',i*2,end='')
    print('\t',i*3)