def locale(**kw): 
    def cbf(f):
        def w(obj):
            obj.lang = kw["language"]
            f(obj)
        return w
    return cbf  

class UserMessageService:
    messages = {"en":"Welcome","fr":"Bonjour"}  
    def show_welcome_message(self):
        print(self.messages[self.lang])
 
