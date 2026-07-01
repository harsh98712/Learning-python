class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"₹{amount} credited successfully.")

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} debited successfully.")
        else:
            print("Insufficient balance!")

    def print_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")


# Creating an object
acc1 = Account(123456789, 5000)

# Printing initial balance
acc1.print_balance()

# Credit money
acc1.credit(2000)
acc1.print_balance()

# Debit money
acc1.debit(3000)
acc1.print_balance()

# Trying to debit more than the balance
acc1.debit(10000)