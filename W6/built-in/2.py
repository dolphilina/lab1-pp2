#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

s = str(input())

upper = []
lower = []

for i in range(len(s)):
    if s[i].isupper():
        upper.append(s[i])
    else:
        lower.append(s[i])

print(len(upper), len(lower))