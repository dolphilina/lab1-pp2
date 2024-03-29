def spy_game(nums):
    code = [0, 0, 7, 'True']
    for num in nums:
        if num == code[0]:
            code.pop(0)
            """
            Если текущее число равно первому элементу кода, то этот элемент удаляется из списка code.
            """
    return len(code) == 1
"""
После прохождения всех чисел из списка nums проверяется, 
остался ли в списке code только один элемент. 
Если да, значит последовательность для шпионского кода была найдена.
"""


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
