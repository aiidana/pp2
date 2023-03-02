# a=list(input())
# def my_func(a):
#     for i in range(len(a)-1):
#         if a[i]==a[i+1]!=3:
#             return False
#         else:
#             return True
# print(my_func(a))
l=list(input())
def has_33(l):
     return any(l[i+1] == l[i] == 3 for i in range(len(l) - 1))
print(has_33(l))