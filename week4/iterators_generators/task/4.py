a,b=int(input()),int(input())
def squares():
    for i in range(a,b+1):
        yield i**2

for i in squares():
    print(i)