class Student:
    def __init__(self, name, adress, phone, course, index_number):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.course = course
        self.index_number = index_number
    
    @staticmethod
    def getinfo(self):
        return (f"Name: {self.name}, Adress: {self.adress}, Phone: {self.phone}"\
                f", Course: {self.course}, Index number: {self.index_number}")
        
drazen_plavsic = Student("Drazen Plavsic", "Sime Solaje 123", "+38765445963", "Informatika", "12/001")
print(Student.getinfo(drazen_plavsic))
simo_perovic = Student("Simo Perovic", "Cara Lazara 2", "+38765223654", "Geografija", "12/002")
print(Student.getinfo(simo_perovic))
jelena_josipovic = Student("Jelena Josipovic", "Trg Oslobodjenja 2", "+38765889632", "Matematika", "12/004")
print(Student.getinfo(jelena_josipovic))