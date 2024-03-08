#Write a Python program with builtin function that returns True if all elements of the tuple are true.

import random

def x(num):
    return True if num > 0 else False

n = int(input("Введите количество элементов: "))

a = tuple(x(random.randint(-100, 100)) for i in range(n))

p = all(a)

for i in a:
    print(i, end=' ')
print()
print(p)