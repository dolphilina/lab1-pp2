import random # Импортируется модуль random, который позволяет генерировать случайные числа.

name = input("Hello! What is your name?\n")

print( f"Well,{name}, I am thinking of a number between 1 and 20.")

num = random.randint(1, 20)
# Генерируется случайное число от 1 до 20, которое пользователь должен будет отгадать.
numb = 0
gss = 0

while numb != num:
    """
Начинается цикл while, который продолжается до тех пор, 
пока догадка пользователя не совпадет с загаданным числом.
    """
    numb = int(input("Take a guess.\n"))
    gss += 1
    if numb < num:
        print("Your guess is too low.")
    elif numb > num:
        print("Your guess is too high.")


print(f"Good job, {name}! You guessed my number in {gss} guesses!")