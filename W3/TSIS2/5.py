"""
Write a function that accepts string from user and print all permutations of that string.
"""
import math
str = str(input()) # str(input()) Принимает только строки.

def permutation(str):
    a = len(str)
    return math.factorial(a)
"""
Возвращает факториал длины строки, 
который представляет собой количество 
возможных перестановок символов в этой строке. 
Для этого используется функция factorial из модуля math.
"""

print(permutation(str))
