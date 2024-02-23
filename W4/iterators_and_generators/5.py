'''
Implement a generator that returns all numbers from (n) down to 0.
'''

def down():
    n = int(input())
    back = (int(i) for i in range (n, -1, -1))
    for i in range(n+1):
        print(next(back))
        
down()
