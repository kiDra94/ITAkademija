class Message():
   message = ""
   def get_message(self):
      return self.message

class User(Message):
   message = "Hello user!"

class Administrator(Message):
   message = "Hello administrator!"

class Director(Message):
   message = "Hello director!"


class UserFactory():
    def create_user(self, type):
        targetclass = type.capitalize()
        return globals()[targetclass]()


user_obj = UserFactory()

user = []
input_user = input("What is your access level?")
user.append(input_user)

for u in user:
   print (user_obj.create_user(u).get_message())
