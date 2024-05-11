class InvalidIdException(Exception): pass
class InvalidFirstNameException(Exception): pass
class InvalidLastNameException(Exception): pass
class InvalidEmailException(Exception): pass

class User():
    def __init__(self, id, firstName, lastName, email):
        if id > 100:
            raise InvalidIdException()
        else:
            self.id = id
        if firstName == "":
            raise InvalidFirstNameException()
        else:
            self.firstName = firstName
        if lastName == "":
            raise InvalidLastNameException()
        else:
            self.lastName = lastName
        if email == "":
            raise InvalidEmailException()
        else:
            self.email = email

try:
    u = User(10, "Petar", "Jackson", "peters@mail.mm")
except InvalidIdException:
    print("Nepravilan ID")
except InvalidFirstNameException:
    print("Nepravilno Ime")
except InvalidLastNameException:
    print("Nepravilno prezime")
except InvalidEmailException:
    print("Nepravilan e-mail")