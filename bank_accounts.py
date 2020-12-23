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
            print("Error: account is closed and is not accepting deposits")
            return
        transaction = {
            "Type": "Deposit",
            "Amount": amount,
            "Source": source
        }
        self.balance += amount
        self.transactions.append(transaction)

    def check_status(self):
        pprint(self.status)
        pprint(self.balance)
        pprint(self.transactions)


account1 = Account()
# account1.check_status()
# account1.deposit(15000, "Mobile")
# account1.check_status()
# account1.deposit(5000, "Online")
# account1.check_status()
