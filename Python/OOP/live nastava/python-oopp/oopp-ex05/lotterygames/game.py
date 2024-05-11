import abc
class game(abc.ABC):
    @abc.abstractmethod
    def pick(self):
        pass
    def get_user_input(self, message): 
        while True:
            try:
                val = int(input(message))
                return val
            except:
                print("Please enter only numeric values")
    
