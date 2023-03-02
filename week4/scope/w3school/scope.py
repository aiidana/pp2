def my_func():
    x=300
    print(x)
my_func()

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

#global scope
x=300
def myfunc():
    print(x)
myfunc()
print(x)#300 300


#The function will print the local x, and then the code will print the global x:
x=300
def myfunc():
    x=200
    print(x)
myfunc()
print(x)
#200 300

#global keyword
def myfunc():
    global x 
    x=300
myfunc()
print(x)
#300


x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)#200

