#if elif else


#An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
  print("b is greater than a")

#if a < b, if  a==b


#ELIF.
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#ELSE
#The else keyword catches anything which isn't caught by the preceding conditions
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#short
if a > b : print("a is greater than b")
print("A") if a > b else print("B")


#and or 
c=3
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")



if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement
