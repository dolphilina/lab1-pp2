"""
A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams
"""
grams = float(input()) # При помощи float(input()) в переменную grams, можно принять число с плавающей запятой.

def convert(grams):
    return grams * 28.3495231 

print(convert(grams)) # Вызываем функцию которая переводит в Унцы
