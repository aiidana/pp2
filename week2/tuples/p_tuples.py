#tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry', 'apple', 'cherry')


thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
#3

thistuple = ("apple",)
print(type(thistuple))
#tuple
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#str


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
"""

('apple', 'banana', 'cherry')
(1, 5, 7, 9, 3)
(True, False, False)

"""

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #<class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple) #('apple', 'banana', 'cherry')


