import messageservice
class UserMessage(messageservice.UserMessageService): 
    @messageservice.locale(language="fr")
    def show_welcome_message(self):
        super().show_welcome_message()
        
ums = UserMessage()
ums.show_welcome_message()