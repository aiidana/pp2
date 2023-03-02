n=int(input())
def my_func():
    for i in range(n):
        yield i**2
for i in my_func():
    print(i)

