'''
Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

'''

def squares():
    a = int(input())
    b = int(input())
    sq = (int(i)**2 for i in range(a, b+1))
    for i in range (b - a + 1):
        print(next(sq))
        
squares()
