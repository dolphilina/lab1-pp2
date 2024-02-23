'''
Create a generator that generates the squares of numbers up to some number N.
'''

def squares():
    n = int(input())
    square = (int(i)**2 for i in range(0, n+1))
    for i in range(n+1):
        print(next(square), end = " ")
        
squares()
