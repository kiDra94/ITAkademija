class decorator:

    def __init__(self,operation):
        self.operation = operation
    def __call__(self,function):
        if self.operation == "+":
            return lambda a,b: a+b
        elif self.operation == "-":
            return lambda a,b: a-b
        elif self.operation == "/":
            return lambda a,b: a/b
        elif self.operation == "*":
            return lambda a,b: a*b

chosen_operation = input("Choose operation: ")
first_number = int(input("First number is: "))
second_number = int(input("Second number is: "))

@decorator(chosen_operation)
def calculate(first_number,second_number):
    pass

print(calculate(first_number,second_number))