#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re 

str = input()

Pattern = '^a(b*)$'
# ^	Starts with
# $  Ends with
# *	Zero or more occurrences
x = re.findall(Pattern, str)

print(x)