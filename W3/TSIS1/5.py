class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def checkBal(self):
        print(f"Balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money on balance")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from deposit")


own1 = Account("Kama^^")
own1.checkBal()
own1.deposit(5000)
own1.checkBal()
own1.withdraw(2000)
own1.checkBal()