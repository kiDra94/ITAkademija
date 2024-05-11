class Card:  
    def __init__(self):
        self.__number    = 0
        self.__color     = ""
        self.__code      = "H1" 
    @property
    def number(self): return self.__number
    @property
    def color(self): return self.__color
    @property
    def code(self): return self.__code 
    @number.setter
    def number(self,val): self.__number = val
    @color.setter
    def color(self,val): self.__color = val
    @code.setter
    def code(self,val): self.__code = val

c = Card()
c.color = "red"
c.number = 11
c.code = "R11"
print(c.color,c.number,c.code)