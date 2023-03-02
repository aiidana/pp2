#arrays

cars = ["Ford", "Volvo", "BMW"]
print(cars)
#['Ford', 'Volvo', 'BMW']


cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x) #ford

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars) #['Toyota', 'Volvo', 'BMW']


cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x) #3


#Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)


cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars) # ['Ford', 'Volvo', 'BMW', 'Honda']


#delete
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars) #['Ford', 'BMW']


cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars) #['Ford', 'BMW']


"""

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

"""
