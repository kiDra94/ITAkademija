class Person:
    def __init__(self,firstname,lastname): 
        self.firstname = firstname
        self.lastname = lastname
    def show(self):
        print(f"Person: {self.firstname} {self.lastname}")

class Student(Person):
    def __init__(self,firstname,lastname,indexnumber):
        super().__init__(firstname,lastname)
        self.indexnumber = indexnumber 

st = Student("Lucky","Luke","123/45")
st.show()