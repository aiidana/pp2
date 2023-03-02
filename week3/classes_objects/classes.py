class MyClass:
    x=5
print(MyClass)
#<class '__main__.MyClass'>



class Myclass:
    x=5

p1=Myclass()
print(p1.x)
#5


class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
p1=Person("John", 36)
print(p1.name)
print(p1.age)
#John 
#36


class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

p1=Person("John", 36)
print(p1)
#<__main__.Person object at 0x2ab9780cd100>

