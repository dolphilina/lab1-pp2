#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

word = input()


left = 0
right = len(word) - 1
flag = True
while left < right:
    if word[left] != word[right]:
        flag = False
        break
    left += 1
    right -= 1

if flag:
    print('Palindrome detected')
else:
    print('Palindrome undetected')