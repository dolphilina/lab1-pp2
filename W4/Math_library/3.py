'''
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''

from math import *

n = int(input("Input number of sides: "))
l = float(input("Input the lenght of a side: "))
apothem = l / (2 * tan(pi / n))
area = int((n * l * apothem) / 2)

print("The area of the polygon is: ", area)