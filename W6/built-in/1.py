#Write a Python program with builtin function to multiply all the numbers in a list

import math

l = []

n = int(input())

for i in range(n):
    i = int(input())
    l.append(i)

res = math.prod(l)

print(res)