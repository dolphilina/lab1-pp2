'''
Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

version 1: divisible by both 3 and 4
'''

def divisibility():
    n = int(input())
    x = lambda x : x if(x % 3 == 0 and x % 4 == 0 and x != 0) else "o"
    a = (x(i) for i in range(0, n))
    for i in range(n):
        y = next(a)
        if(y != "o"):
            print(y)

divisibility()
