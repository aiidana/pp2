n=int(input())

def my_func():
    for i in range(0,n):
        if (i%4==0) and (i%3==0):
            yield i 

for i in my_func():
    print(i)

