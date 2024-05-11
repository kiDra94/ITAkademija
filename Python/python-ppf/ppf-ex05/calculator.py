a = int(input('Enter first operand? '))
b = int(input('Enter second operand? '))
op = input('Choose operation (add,sub,mul,div): ')

if(op=='add'):
    print("Result is: ", a + b) 
elif(op=='sub'):
    print("Result is: ", a - b)
elif(op=='mul'):
    print("Result is: ", a * b)
elif(op=='div'):
    print("Result is: ", a / b)
else:
    print("Unknown operation")
