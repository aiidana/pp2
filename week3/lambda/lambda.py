#lambda arguments : expression

x=lambda a:a+10
print(x(5))#15

x=lambda a,b: a* b
print(x(5,6))
#30

x=lambda a,b,c: a+b+c
print(x(5,6,7))
#or 
print((lambda a,b,c:a+b+c)(5,6,7))


#function and lambda
def my_func(n):
    return lambda a:a*n

mydoubler= my_func(2)
print(mydoubler(11))#22



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))#22 and 33


