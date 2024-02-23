'''
Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

between(0 < numbers < n)
'''

def evens():
    n = int(input())
    even = (int(i) for i in range(2, n - 1, 2))
    for i in range(int(n / 2) - 2):
        print(next(even), end = ", ")
    print(next(even))

evens()