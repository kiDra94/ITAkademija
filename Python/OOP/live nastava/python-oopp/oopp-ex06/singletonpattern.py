class MyClass: 
    __instance = None 
    @staticmethod
    def get_instance():
        if not MyClass.__instance:
            MyClass.__instance = MyClass()
        return MyClass.__instance

    def __init__(self):
        if not MyClass.__instance:
            MyClass.__instance = self
        else:
            raise Exception("Cannot Instantiate")
        
a = MyClass.get_instance()
b = MyClass.get_instance()

print(a == b)


 