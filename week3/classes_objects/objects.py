class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def my_func(self):
        print("Hello my name is "+ self.name)

p1=Person("John", 36)
p1.my_func()
#Hello my name is John


class Person:
    def __init__(mysillyobject, name , age):
        mysillyobject.name=name
        mysillyobject.age=age
    
    def myfunc(abc):
        print("hello my name is "+abc.name)
p1=Person("John", 36)
p1.myfunc()
#Hello my name is John


class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age

p1=Person("John",36)
p1.age=40
print(p1.age)
#40

class Person:
  pass
#having an empty class definition like this, would raise an error without the pass statement