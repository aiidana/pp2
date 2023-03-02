
class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality= nationality

    def info(self):
        print("name : "+self.name) 
        print("nationality :",self.nationality)

    def setSurname(self, surname):
        self.surname=surname

    def getSurname(self):
        print(self.surname)


class Student(Person):
    def __init__(self, name, nationality, id):
        super().__init__(name, nationality)
        self.id=id

    def info(self):
        super().info()
        print("id:",self.id)
    

x=Student("Aidana", "kazakh", "22B050850")
print(x.info())
print(x.setSurname("Koshkinbayeva"))
print(x.getSurname())

class Teacher:
    def __init__(self, t_name, t_nationality, teacher_id):
        # super().__init__(t_name, t_nationality)
        self.t_name=t_name
        self.t_nationality=t_nationality
        self.teacher_id=teacher_id

    def inform(self):
        # super().info()
        print("teacher's name : "+self.t_name)
        print("teacher's nationality :", self.t_nationality)
        print("teacher's id:", self.teacher_id)

teacher=Teacher("Arnur","kazakh", "22123456")
teacher.inform()