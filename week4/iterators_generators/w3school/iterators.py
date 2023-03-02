mytuple=("apple","banana", "cherry")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))#apple banana cherry


str="banana"
myit= iter(str)
print(next(myit)) #b
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a

mytuple=("apple", "banana", "cherry")
for x in mytuple:
    print(x)#apple banana cherry

mystr = "banana"
for x in mystr:
  print(x)
"""
b
a
n
a
n
a
"""

#classes and objects
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

myclass=MyNumbers()
myiter=iter(myclass)
print(next(myiter)) #1
print(next(myiter)) #2
print(next(myiter)) #3

#stop after 20
class Numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=Numbers()
myiter=iter(myclass)

for x in myiter:
    print(x)