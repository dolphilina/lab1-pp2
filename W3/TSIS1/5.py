class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    """
    __init__: Метод-конструктор класса, 
    который инициализирует атрибуты счета при его создании: 
    owner (владелец счета) и balance (баланс счета, изначально 0).
    """
    def checkBal(self):
        print(f"Balance is {self.balance}")
    #checkBal: Метод, который выводит текущий баланс счета.
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited")
    """
    deposit: Метод, который позволяет владельцу счета 
    внести деньги на счет (увеличивает баланс на указанную сумму).
    """
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money on balance")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from deposit")
    """
    withdraw: Метод, который позволяет владельцу счета снять деньги 
    cо счета (уменьшает баланс на указанную сумму), 
    предварительно проверяя, 
    достаточно ли денег на счете для снятия заданной суммы.
    """

# Далее, создается объект own1 класса Account с владельцем "Yipppeeee". Затем вызываются методы этого объекта для демонстрации его функциональности:
own1 = Account("Yipppeeee")
own1.checkBal() #checkBal(): Печатает начальный баланс счета (0).
own1.deposit(5000) #deposit(5000): Вносит на счет 5000 денег.
own1.checkBal() #checkBal(): Печатает текущий баланс счета (5000).
own1.withdraw(2000) #withdraw(2000): Снимает со счета 2000 денег.
own1.checkBal() #checkBal(): Печатает текущий баланс счета после снятия (3000).