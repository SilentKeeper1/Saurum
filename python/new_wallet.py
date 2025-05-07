class Wallet:
    def __init__(self, currency, initial_balance):
        self.currency = currency
        self.balance = initial_balance

    def display_wallet_info(self):
        print(f"Currency: {self.currency}")
        print(f"Balance: {self.balance}")

new_wallet = Wallet(currency="USD", initial_balance=1000)

new_wallet.display_wallet_info()
