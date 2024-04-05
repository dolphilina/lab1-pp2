#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

word = input()


word1 = word[::-1]
if word1 == word:
    print('Palindrome detected')
else:
    print('Palindrome undetected')
