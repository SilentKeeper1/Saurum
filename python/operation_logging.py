#6) Логуйте всі операції з кошельками для можливості відстеження історії транзакцій користувача.

class Wallet:
    def __init__(self, currency, initial_balance):
        self.currency = currency
        self.balance = initial_balance
        self.transaction_history = []

    def add_funds(self, amount, note="Deposit"):
        self.balance += amount
        self.transaction_history.append(
            f"Added {amount} {self.currency} - {note}. Current balance: {self.balance}"
        )

    def subtract_funds(self, amount, note="Withdrawal"):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transaction_history.append(
            f"Subtracted {amount} {self.currency} - {note}. Current balance: {self.balance}"
        )

    def display_transaction_history(self):
        print(f"Transaction History for {self.currency} Wallet:")
        for transaction in self.transaction_history:
            print(transaction)

wallet = Wallet("USD", 1000)

wallet.add_funds(200, "Salary")
wallet.subtract_funds(150, "Shopping")
wallet.add_funds(50, "Gift")
wallet.subtract_funds(100, "Bills")
wallet.display_transaction_history()