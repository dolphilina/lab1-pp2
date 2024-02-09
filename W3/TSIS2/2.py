"""
Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)
"""

f = float(input()) # При помощи float(input()) в переменную grams, можно принять число с плавающей запятой.

def f_to_c(f):
    return (5 / 9) * (f - 32)

print(f_to_c(f)) # Вызывает функцию которая с Фаренгейта переводит в цельсий