class Wallet:
    def __init__(self, currency, initial_balance):
        self.currency = currency
        self.initial_balance = initial_balance
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

    def reset_wallet(self, reset_note="Reset to initial balance"):
        self.balance = self.initial_balance
        self.transaction_history.append(
            f"Wallet reset - {reset_note}. Current balance: {self.balance}"
        )

    def display_transaction_history(self):
        print(f"Transaction History for {self.currency} Wallet:")
        for transaction in self.transaction_history:
            print(transaction)

wallet = Wallet("USD", 1000)

wallet.add_funds(200, "Salary")
wallet.subtract_funds(150, "Shopping")

print("Before reset:")
wallet.display_transaction_history()

wallet.reset_wallet()

print("\nAfter reset:")
wallet.display_transaction_history()