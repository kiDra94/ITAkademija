# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    def __init__(self):
        print("Izuzetak osnovne klase")


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    def __init__(self):
        print("Izuzetak klase ValueTooSmallError")
        
    def metoda(self):
        print("Poziva se metoda iz klase ValueTooSmallError")
        
    def __str__(self):
        return "GRESKA - klasa ValueTooSmallError"


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    def __init__(self):
        print("Izuzetak osnovne klase ValueTooLargeError")

# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError as v:
        print("This value is too small, try again!")
        v.metoda()
        print(v)
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")



#help(Exception)
#help(Error)
#help(ValueTooSmallError)