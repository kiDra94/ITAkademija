import enum
class User:
    def login(self):
        print("User login")
class Admin:
    def login(self):
        print("Admin login")
class SuperAdmin:
    def login(self):
        print("SuperAdmin login")

class UserType(enum.Enum):
    User        = 1
    Admin       = 2
    SuperAdmin  = 3

class UserFactory: 
    @staticmethod
    def get_user(user_type):
        if user_type == UserType.User:
            return User()
        elif user_type == UserType.Admin:
            return Admin()
        elif user_type == UserType.SuperAdmin:
            return SuperAdmin()
        
user = UserFactory.get_user(UserType.Admin)
user.login()
 