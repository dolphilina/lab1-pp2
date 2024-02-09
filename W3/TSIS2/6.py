"""Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
"""

s = str(input())

def reverse(s):
    a = s.split()
    """
    a = s.split(): Разбивает строку s на список слов с помощью метода split(). По умолчанию split() разбивает строку по пробелам, создавая список слов.
    """
    a.reverse()
    """
    Меняет порядок элементов списка a на обратный с помощью метода reverse().
    """
    return a

print(reverse(s))