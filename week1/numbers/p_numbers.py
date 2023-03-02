#three numeric types in Python:
#int float complex

x = 1
y = 2.8
z = 1j
print(type(x))#int
print(type(y))#float
print(type(z))#complex

x = 1
y = 35656222554887711
z = -3255522
print(type(x))#int
print(type(y))#int
print(type(z))#int


x = 1.10
y = 1.0
z = -35.59
print(type(x))#float
print(type(y))#float
print(type(z))#float


#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j



x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)


#random
import random
print(random.randrange(1, 10))