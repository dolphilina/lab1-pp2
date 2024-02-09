"""
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
"""

def filter_prime(my_list):
    l = []
    for i in my_list:
        cnt = 0
        if(i == 2):
            l.append(i)
            continue
        elif(i == 1):
            continue
        for j in range(2, i):
            if(i % j == 0):
                cnt += 1
        if(cnt == 0):
            l.append(i)
    """
Для каждого числа i проверяется, является ли оно простым:

Если i равно 2, то оно добавляется в список l, так как 2 является простым числом.
Если i равно 1, происходит переход к следующей итерации без изменений.
Для всех остальных чисел i от 3 до i-1 происходит проверка деления i на j. Если хотя бы одно такое деление без остатка произойдет, значит i не является простым числом, и переменная cnt увеличится на 1.
Если после проверки всех возможных делителей для i переменная cnt останется равной 0, то число i добавляется в список l, так как оно простое.
    """
    return l #После прохождения всех чисел из списка возвращается список l, содержащий только простые числа.

print(filter_prime([2,6, 7, 9]))
