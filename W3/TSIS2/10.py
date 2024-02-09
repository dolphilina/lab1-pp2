"""Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set."""

def unique(dupl):
    newlist = [] # Создается пустой список newlist, который будет содержать только уникальные элементы.
    for n in dupl:
        if n not in newlist: # Проверяется, присутствует ли текущий элемент n в списке newlist.
            newlist.append(n) # Если текущий элемент n не содержится в списке newlist, он добавляется в этот список.
    return newlist
    
dupl = []
a = int(input())
for i in range(a):
    dupl.append(int(input())) #Для каждого числа в диапазоне добавляется в список dupl, преобразованное в целое число.

print(unique(dupl))