class Person:
    def __init__(self,fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

x=Person("John", "Doe")
x.printname()
#John Doe

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x=Student("Mike", "Olsen")
x.printname()
#Mike Olsen


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
#Mike Olsen


#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
x=Student("Mike", "Olsen")
x.printname()


#add method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)
#2019


class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fnama, lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year

x=Student("Mike","Olsen", 2019)
print(x.graduationyear)
#2019



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome",self.firstname, self.lastname,"to the class of",self.graduationyear)

x=Student("Mike", "Olsen", 2019)
x.welcome()
#Welcome Mike Olsen to the class of 2019


