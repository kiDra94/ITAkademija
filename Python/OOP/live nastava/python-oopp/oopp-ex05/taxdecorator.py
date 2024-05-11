def tax(func,*args): 
    def wrapper(*args):
        return func(args[0],args[1],args[2]) * 1.2
    return wrapper 
  
class Calc(object): 
    @tax
    def do(self, x, y):
        return x + y

c = Calc()
print("{:.2f}".format(c.do(4,5)))


