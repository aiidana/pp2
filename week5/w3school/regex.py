
"""
findall       returns a list containing all matches
search        returns a match object if there is a match anywhere in the string
split         returns a list where the string has been split at each match
sub           replaces one or many matches with a string

"""
"""
[]     a set of characters          f.e "[a-m]"
\      signals a special sequence   f.e "\d"
.	   Any character (except newline character)	"he..o"	
^	   Starts with	"^hello"	
$	   Ends with	"planet$"	
*	   Zero or more occurrences	"he.*o"	
+	   One or more occurrences	"he.+o"	
?	   Zero or one occurrences	"he.?o"	
{}	   Exactly the specified number of occurrences	"he.{2}o"	
|	   Either or	"falls|stays"	
()	   Capture and group
 """
import re 
text="The rain in Spain"
x=re.search("^The.*Spain$", text)

if x:
    print("Yes! We have a match!")
else:
    print("No match")


"""
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
    r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
    r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
"""
import re
txt="The rain in Spain"
x=re.findall("ai",txt)
print(x)
#['ai','ai']



import re 
txxt="the rain in Spain"
x=re.search("\s",txxt)
print("The first white- space character is located in position:", x.start())#3


import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)#none

import re
#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)#['The', 'rain', 'in', 'Spain']

import re
#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
#['The', 'rain in Spain']

import re
#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)#The9rain9in9Spain

import re
#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)#The9rain9in Spain

import re
#The search() function returns a Match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)#<_sre.SRE_Match object; span=(5, 7), match='ai'>

import re
#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#12 17


import re
#The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#The rain in Spain

import re
#Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
#Spain




