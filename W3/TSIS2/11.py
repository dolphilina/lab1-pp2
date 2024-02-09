"""Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""
s = str(input())

def palindrome(s):
    if s == s[::-1]: 
#Сравнивается исходная строка s с её обратной версией, полученной с помощью среза [::-1], который разворачивает строку задом наперёд.
        return True
    else:
        return False

print(palindrome(s))

