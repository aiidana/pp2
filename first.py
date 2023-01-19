# print ('hello world')
# def hello():
#     print ('hello world')
# hello()

# x= int(input())
# y= int(input())
# def sum(a,b):
#     return a+b
# print(sum(x,y))


# a=45
# def h():
#     global a
#     a= a+2
#     print(a)
# h()
# print(a)

# name =input()
# a= int(input())
# b= int(input())
# for i in name:
#     print(i)
# print(a+b)

# a=1
# for i in range(1,11):
#     print(i)
#     i+=1

# i=1
# while i<=10 :
#     print(i)
#     i+=1

# for i in range(1,11):
#     int(input())
#     print(i)

# a=int(input())

# def x ():
#     return a*a


# print(x())



# import re
# s='AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
# result = re.match('AC', s)
# print(result)

# import re
# s='AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
# result = re.search('/', s)#findall
# print(result)

# import re
# s='AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
# result = re.split('/', s)
# print(result)

# print((lambda a,b : a if a>b else b)(23,14))

# print((lambda a : 4*a)(a=int(input())))

# print((lambda a,b,c : (a+b+c)/3)(a=int(input()), b=int(input()), c=int(input())))

# n=int(input())
# for x in range(n):
#     x=int(input())
#     if x%2==0:
#         print('even')
#     else :print('odd')



# import turtle

# ai=turtle.Turtle()

# for i in range(50):
#     ai.forward(150)
#     ai.right(135)


# print((lambda a, b ,c : a*b*c/2)(a=int(input('a=')),b=int(input('b=')),c=int(input('c='))))

from turtle import *
color('red', 'yellow')

begin_fill()
while True:
    speed(10)
    forward(200)
    left(170)
   
end_fill()
done()
