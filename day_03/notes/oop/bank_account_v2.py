class BankAccount:
    def __init__(self, initial_balance=0):
        # Data/Variable
        self.balance = initial_balance

    # Method/Function: deposit
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.balance += amount

    # Method/Function: withdraw
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        elif amount > self.balance:
            raise ValueError("Amount cannot be greater than balance")

        self.balance -= amount

    # Method/Function: print_balance
    def print_balance(self):
        print(self.balance)

myaccount = BankAccount()
myaccount.deposit(100)
myaccount.print_balance()
myaccount.withdraw(100)
myaccount.print_balance()