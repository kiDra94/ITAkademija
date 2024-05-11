while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"{a} + {b} = {a + b}")
    except:
        print("Error entry, please try again")