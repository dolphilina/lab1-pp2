#Write a function that computes the volume of a sphere given its radius.

from math import pi

r = float(input()) # При помощи float(input()) в переменную grams, можно принять число с плавающей запятой.

def volume(r):
    v = (4/3) * pi * (r ** 3)
    return v

print(volume(r))