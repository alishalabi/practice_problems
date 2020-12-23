"""
Introduction
Simulate a bank account supporting opening/closing, withdrawals, and deposits of money. Watch out for concurrent transactions!

A bank account can be accessed in multiple ways. Clients can make deposits and withdrawals using the internet, mobile phones, etc. Shops can charge against the account.

Create an account that can be accessed from multiple threads/processes (terminology depends on your programming language).

It should be possible to close an account; operations against a closed account must fail.

"""

"""
Assumption: Sample account
account = {
    status: "Open",
    balance: 15000,
    transactions: [
        {
        type: "Deposit",
        amount: 15000,
        source: "Mobile"
        }
    ]
}
"""

from pprint import pprint


class Account:
    def __init__(self):
        self.status = "Open"
        self.balance = 0
        self.transactions = []

    def deposit(self, amount, source):
        if self.status == "Closed":
            print("Error: account is closed and is not accepting deposits.")
            return
        new_balance = self.balance + amount
        transaction = {
            "Type": "Deposit",
            "Amount": amount,
            "Source": source,
            "Balance after transaction": new_balance
        }
        self.balance = new_balance
        self.transactions.append(transaction)

    def withdraw(self, amount, source):
        if self.status == "Closed":
            print("Error: account is closed and is not accepting deposits.")
            return
        if amount > self.balance:
            print(f"Insufficient balance to withdraw {amount}. Please withdaw up to {self.balance}.")
            return
        new_balance = self.balance - amount
        transaction = {
            "Type": "Withdraw",
            "Amount": amount,
            "Source": source,
            "Balance after transaction": new_balance
        }
        self.balance = new_balance
        self.transactions.append(transaction)

    def close_account(self):
        self.status = "Closed"

    def open_account(self):
        self.status = "Open"

    def check_status(self):
        pprint(self.status)
        pprint(self.balance)
        pprint(self.transactions)


account1 = Account()
# account1.check_status()
account1.deposit(15000, "Mobile")  # Balance: 15000
# account1.check_status()
account1.deposit(5000, "Online")  # Balance: 20000
# account1.check_status()
account1.withdraw(10000, "ATM")  # Balance: 10000
# account1.check_status()
account1.withdraw(1000000, "ATM")  # Should show error message
account1.close_account()
# account1.withdraw(10, "Shopping")  # Should show error message
# account1.deposit(10, "Online")  # Should show error message
account1.open_account()
account1.withdraw(1000, "Shopping")  # Balance: 9000
# account1.check_status()
account1.deposit(10000, "Mobile")  # Balance: 19000
account1.check_status()
