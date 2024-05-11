def fibonacci(max):
    a, b = 0, 1            
    while a < max:
        yield a           
        a, b = b, a + b   
        
for n in fibonacci(10):
	print(n, end=' ')
