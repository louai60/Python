class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient funds: Charging a TND5 fee")
            self.balance -= 5
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  

    def create_account(self, acc_name, int_rate=0.02, balance=0):
        self.accounts[acc_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, acc_name, amount):
        if acc_name in self.accounts:
            self.accounts[acc_name].deposit(amount)
        else:
            print("account not found.")
        return self

    def make_withdrawal(self, acc_name, amount):
        if acc_name in self.accounts:
            self.accounts[acc_name].withdraw(amount)
        else:
            print("account not found.")
        return self

    def display_user_balance(self, acc_name):
        if acc_name in self.accounts:
            print(f"User: {self.name}, account: {acc_name}, balance: TND{self.accounts[acc_name].balance}")
        else:
            print("account not found.")
        return self



# Testing
user1 = User("Louay", "louay@example.com")
user1.create_account("checking", balance=1000).create_account("savings", balance=500)

user2 = User("joe", "joe@example.com")
user2.create_account("savings", balance=1500)

user1.make_deposit("checking", 200).make_withdrawal("checking", 50).display_user_balance("checking")

user1.display_user_balance("checking")
user2.display_user_balance("savings")
