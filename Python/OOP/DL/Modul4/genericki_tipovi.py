from typing import TypeVar
 

def greet(name):
    return print("Hello " + name)
greet("john")
#greet(123) #greska u tipu

T = TypeVar("T")

def blank(first:T, second:T) -> None:
    pass

blank(11,2)
blank("ja", 123)
blank(blank(1,2), blank("abc", "abc"))