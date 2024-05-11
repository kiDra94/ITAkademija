def decorator(operation):
    def inner(function):
        if operation == "+":
            return lambda a,b: a+b
        elif operation == "-":
            return lambda a,b: a-b
        elif operation == "/":
            return lambda a,b: a/b
        elif operation == "*":
            return lambda a,b: a*b
        return function
    return inner


chosen_operation = input("Choose operation: ")
first_number = int(input("First number is: "))
second_number = int(input("Second number is: "))

@decorator(chosen_operation)
def calculate(first_number,second_number):
    pass

print(calculate(first_number,second_number))



