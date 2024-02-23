class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

def print_accounts(accounts):
    for account in accounts:
        account.display_account_info()

account1 = BankAccount(0.02, 100)
account2 = BankAccount()

account1.deposit(50).deposit(100).deposit(200).withdraw(75).yield_interest().display_account_info()
account2.deposit(200).deposit(300).withdraw(100).withdraw(50).withdraw(25).withdraw(75).yield_interest().display_account_info()

print_accounts([account1, account2])
