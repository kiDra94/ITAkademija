class MyException(Exception):
    def __str__(self):
        return "Something nice"

def throwingEx():
    raise MyException()

def throwingEx1():
    throwingEx()

try:
    throwingEx1()
except MyException as ex:
    print("Error in function") 
        
try:
    raise MyException()
except MyException as ex:
    print("Hey, this is same as regular Exception") 
    print(f"Custom exception text: {ex}")