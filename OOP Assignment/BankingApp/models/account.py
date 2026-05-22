from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        self.get_balance()

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance
    

    
class SavingsAccount(Account):
    MIN_BALANCE = 1000.0
    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)

    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            self.get_balance()


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 5000.0
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        available_funds = self.balance + self.OVERDRAFT_LIMIT
        if amount > available_funds:
            print("Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            self.get_balance()