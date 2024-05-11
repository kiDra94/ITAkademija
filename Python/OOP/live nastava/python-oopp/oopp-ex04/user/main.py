class User():
    def __init__(self, id, firstName, lastName, email):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

u = User(10, "Petar", "Jackson", "peters@mail.mm")
print(u)