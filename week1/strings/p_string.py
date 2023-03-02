#Strings in python are surrounded by either single quotation marks, or double quotation marks
#'hello' is the same as "hello"

#i can use three double quotes or three single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#position
a = "Hello, World!"
print(a[1])#e

#size/length
a = "Hello, World!"
print(len(a))#13

x = "The best things in life are free!"
print("free" in x) #true

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)



#slicing strings
b = "Hello, World!"
print(b[2:5])#llo
b = "Hello, World!"
print(b[:5])#Hello
b = "Hello, World!"
print(b[2:])#llo, World!
b = "Hello, World!"
print(b[-5:-2]) #orl


#modify strings
a = "Hello, World!"
print(a.upper())#upper
print(a.lower())#lower
print(a.replace("H", "J"))#Jello, World!
print(a.split(",")) # returns ['Hello', ' World!']


#concatenate strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = "Hello"
b = "World"
c = a + b
print(c)

#format strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #I want to pay 49.95 dollars for 3 pieces of item 567


"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""