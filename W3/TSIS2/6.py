"""Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
"""

s = str(input())

def reverse(s):
    a = s.split()
    a.reverse()
    return a

print(reverse(s))