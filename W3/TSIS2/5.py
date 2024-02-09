"""
Write a function that accepts string from user and print all permutations of that string.
"""
import math
str = str(input())

def permutation(str):
    a = len(str)
    return math.factorial(a)

print(permutation(str))
