"""Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:
"""

def histogram(nums):
    for i in nums:
        for j  in range(i):
            print("*", end = "") # В каждой итерации внутреннего цикла выводится звездочка без перевода строки.
        print()
     
histogram([4, 6 ,7])
"""
python 12.py


****
******
*******
"""