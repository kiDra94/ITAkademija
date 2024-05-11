class Alphabet:
    def __init__(self, value):
        self._value = value
 
    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value
 
    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value
 
    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value
 
    value = property(getValue, setValue, 
                     delValue, )
 
a = Alphabet('s')
print(a.value)
#print(a.getValue())
a.value = '7'
print(a.__dict__)
del a.value
print(a.__dict__)
#print(a.value)