n=int(input())
def my_func():
    for i in range(n,0,-1):
        yield i

for i in my_func():
    print(i)