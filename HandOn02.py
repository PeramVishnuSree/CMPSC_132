# object oriented programming part 02
# model a bank account with support for deposit and withdraw operations

class Account:

    def __init__(self, name):
        self.holder = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Not enough funds'

        self.balance -= amount
        return self.balance
