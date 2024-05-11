# Python program to explain property()
# function using decorator
 
class Alphabet:
    def __init__(self, value):
        self._value = value
 
    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value
 
    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value
 
    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value
 
a = Alphabet('s')
print(a.value)
#print(a.getValue())
a.value = '7'
print(a.__dict__)
del a.value
print(a.__dict__)
#print(a.value)
